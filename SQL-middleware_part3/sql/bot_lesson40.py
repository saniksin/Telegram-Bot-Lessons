"""
examples
program model
finite-state-machine
"""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage #содержим данные о состояния
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


from config import TOKEN_API, HELP_COMMAND
from sqlite import db_start, create_profile, edit_profile, show_profile

async def on_startup(_):
    await db_start()

storage = MemoryStorage() #хранит данные состояния бота
bot = Bot(TOKEN_API)
dp = Dispatcher(bot=bot,
                storage=storage)

def get_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('/create'), KeyboardButton('/help'))
    kb.add(KeyboardButton('Show profile!'))

    return kb

def cancel_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/cancel'))

class ProfileStatesGroup(StatesGroup): #Класс который будет хранить состояния бота

    photo = State()
    name = State()
    age = State()
    description = State()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Welcome! So as to create profil - type /create',
                         reply_markup=get_kb())
    
    await create_profile(user_id=message.from_user.id)

@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message) -> None:
    await message.answer(HELP_COMMAND, parse_mode="HTML")
    await message.delete()

@dp.message_handler(Text(equals='Show profile!'))
async def command_showpf(message: types.Message):
    await message.delete()
    profile = await show_profile(message.from_user.id)
    await bot.send_photo(chat_id=profile[0],
                         photo=profile[1],
                         caption=f"""Name: {profile[2]}\nAge: {profile[3]}\nDescription: {profile[4]}""")

@dp.message_handler(commands=['cancel'], state="*")
async def cmd_cancel(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return 
    else:
        await message.reply('Действие отменено',
                        reply_markup=get_kb())
        await state.finish()

@dp.message_handler(commands=['create'])
async def cmd_create(message: types.Message) -> None:
    await message.reply('Let`s create your profile! To begin with, send me your photo!',
                        reply_markup=cancel_kb())
    await ProfileStatesGroup.photo.set() #устанавливаем первое состояние, фото

@dp.message_handler(lambda message: not message.photo, state=ProfileStatesGroup.photo)
async def check_photo(message: types.Message) -> None:
    return await message.reply('Это не фотография')

@dp.message_handler(content_types=['photo'], state=ProfileStatesGroup.photo) #Контент только фото и только если установлен режим фото
async def cmd_photo(message: types.Message, state: FSMContext) -> None: # state: FSMContext состояния автомата
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    await message.reply('Фото сохранено!\nА теперь отправь свое имя!')
    await ProfileStatesGroup.next()

@dp.message_handler(state=ProfileStatesGroup.name) #Только если установлен статус имени
async def cmd_name(message: types.Message, state: FSMContext) -> None: # state: FSMContext состояния автомата
    async with state.proxy() as data:
        data['name'] = message.text

    await message.reply('Имя сохранено!\nА теперь отправь свой возвраст!')
    await ProfileStatesGroup.next()

@dp.message_handler(lambda message: not message.text.isdigit() or int(message.text) < 16 or int(message.text) > 100, state=ProfileStatesGroup.age)
async def check_age(message: types.Message) -> None:
    if int(message.text) < 16:
        return await message.reply('Ваш возвраст не позволяет пользоваться приложением')
    else:
        return await message.reply('Возвраст неверно указан')

@dp.message_handler(state=ProfileStatesGroup.age) #Только если установлен статус возвраста
async def cmd_age(message: types.Message, state: FSMContext) -> None: # state: FSMContext состояния автомата
    async with state.proxy() as data:
        data['age'] = message.text

    await message.reply('Cохранено!\nА теперь расскажи немного о себе!')
    await ProfileStatesGroup.next()

@dp.message_handler(state=ProfileStatesGroup.description) #Только если установлен статус description
async def cmd_description(message: types.Message, state: FSMContext) -> None: # state: FSMContext состояния автомата
    async with state.proxy() as data:
        data['description'] = message.text
        print(data)

    await edit_profile(state, user_id=message.from_user.id)
    await message.reply('Ваша анкета успешно создана!')
    
    async with state.proxy() as data:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=data['photo'],
                             caption=f"Имя: {data['name']}\nВозвраст: {data['age']}\nО себе: {data['description']}")
    
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)