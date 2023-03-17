from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import HELP_COMMAND, TOKEN_API
import random

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('Отправить апельсин')
b3 = KeyboardButton('/random')
kb.add(b1).insert(b2).insert(b3)

@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text="Добро пожаловать. Выберите одну из опций на клавиатуре",
                           reply_markup=kb)

@dp.message_handler(commands=["help"])
async def command_help(message: types.Message):
    await message.answer(text=HELP_COMMAND,
                         parse_mode="HTML")
    await message.delete()

@dp.message_handler(commands=["description"])
async def command_description(message: types.Message):
    await message.reply(text="Бот показывает функционал клавиатуры")

@dp.message_handler(commands=['random'])
async def command_random(message: types.Message):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    await bot.send_location(chat_id=message.chat.id,
                            latitude=y,
                            longitude=x
                            )


@dp.message_handler()
async def command_emoji(message: types.Message):
    if message.text == '❤️':
        await bot.send_sticker(chat_id=message.chat.id,
                               sticker='CAACAgIAAxkBAAPEZA5tkSIRgni1x7zfqRfDloCMc9AAAocbAAIIGTBK_PI5fpFznkUvBA')
    if message.text == 'Отправить апельсин':
        await bot.send_photo(chat_id=message.chat.id,
                       photo='https://suseky.com/wp-content/uploads/2015/06/222.jpg')



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)