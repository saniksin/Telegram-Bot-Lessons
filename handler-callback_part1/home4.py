from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
import string #модуль с буквами
import random

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

count = 0

@dp.message_handler(commands=["random"])
async def random_letter(message: types.Message):
    await message.reply(text=random.choice(string.ascii_letters))

@dp.message_handler(commands=["description"])
async def command_description(message: types.Message):
    await message.answer(text='Бот выдает одну рандомную букву английского языка.')
    await message.delete()

@dp.message_handler(commands=["count"])
async def command_count(message: types.Message):
    global count 
    count += 1
    await message.reply(text=f'Команда вызывалась {count} раз')

@dp.message_handler()
async def check_zero(message: types.Message):
    if '0' in message.text:
        await message.answer(text='YES')
    else:
        await message.answer(text='NO')


if __name__ == '__main__':
    executor.start_polling(dp)