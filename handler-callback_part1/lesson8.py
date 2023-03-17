"""
Клавиатура = 
ReplyKeyboardMarkup = resize_keyboard (подстроить под окно), one_time_keyboard создать клавиатуру
KeyboardButton = text создать кнопку
ReplyKeyboardRemove = закрыть клавиатуру
"""

from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API, HELP_COMMAND
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

# resize_keyboard (подстроить под окно)
kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/photo')
b3 = KeyboardButton('/description')
kb.add(b1).insert(b2).insert(b3)



@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode="HTML",)
    await message.delete()

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Добро пожаловать в наш бот",
                           parse_mode="HTML",
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=["description"])
async def description_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Наш бот умеет отправлять фотографии.",
                           parse_mode="HTML")
    await message.delete()

@dp.message_handler(commands=["photo"])
async def photo_command(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                        photo="https://i.pinimg.com/736x/ba/92/7f/ba927ff34cd961ce2c184d47e8ead9f6.jpg")
    await message.delete()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)