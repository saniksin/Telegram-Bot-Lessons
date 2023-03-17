"""
1) from aiogram.contrib.fsm_storage.memory import MemoryStorage
2) dp = Dispatcher(bot=bot, storage=storage)
3) Состояния класс который наследуется от StateGroup
4) from aiogram.dispatcher.filters.state import StatesGroup, State
5) from aiogram.dispatcher import FSMContext
6) В классе создаем атрибут класса и даем ему значение State
7) State - это состояния которые будут использоваться ботом
8) Создали кнопку отмены состояний (команда /cancel)
9) Передали туда аргумент state: FSMContext
10) в /cancel обработали завершение состояния await state.finish()
11) Далее в начать работу устанавлием состояние await ClientStatesGroup.photo.set()
12) Если пользователь высылает фото сохраняем фото async with state.proxy() as data
13) Меняем состояние await ClientStatesGroup.next()
14) После добавление описания пишем сохраняем текст
15) Далее state.finish()
"""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from config import TOKEN_API

storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot=bot,
                storage=storage)

class ClientStatesGroup(StatesGroup):
    photo = State()
    desc = State()


def get_keyboard() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton('Начать работу!'))
    return kb

def get_cancel() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/cancel'))

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer('Добро пожаловать',
                         reply_markup=get_keyboard())

@dp.message_handler(commands=['cancel'], state='*')
async def cmd_cancel(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    
    await message.reply('Дейстие отменено!',
                        reply_markup=get_keyboard())
    await state.finish()

@dp.message_handler(Text(equals='Начать работу!', ignore_case=True), state=None)
async def cmd_startwork(message: types.Message) -> None:
    await ClientStatesGroup.photo.set()
    await message.answer('Сначала отправь нам фотографию!',
                         reply_markup=get_cancel())

@dp.message_handler(lambda message: not message.photo, state=ClientStatesGroup.photo)
async def check_photo(message: types.Message) -> None:
    return await message.reply('Это не фотография!')

@dp.message_handler(lambda message: message.photo, content_types=['photo'], state=ClientStatesGroup.photo)
async def load_photo(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

    await ClientStatesGroup.next()
    await message.reply('А теперь отправь нам описание!')

@dp.message_handler(state=ClientStatesGroup.desc)
async def load_photo(message: types.Message, state: FSMContext) -> None:
    async with state.proxy() as data:
        data['desc'] = message.text

    await message.reply('Ваша фотография сохранена')

    async with state.proxy() as data:
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=data['photo'],
                             caption=data['desc'])
        
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)