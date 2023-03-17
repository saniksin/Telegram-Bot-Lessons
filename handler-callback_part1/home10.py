from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from config import TOKEN_API
from module_home_10 import ikb

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_starup(_):
    print('Я запустился!')


kb = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
butt1 = KeyboardButton('/links')
kb.add(butt1)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Добро пожаловать!',
                           reply_markup=kb)


@dp.message_handler(commands=['links'])
async def command_links(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text='Доступные ссылки',
                           reply_markup=ikb)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_starup)