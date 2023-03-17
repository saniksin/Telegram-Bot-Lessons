# Задача 1
# Напишите бота который будет отправлять пользователю его же сообщение, переведенное в верхний регистр.

from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

# Задача 1
# @dp.message_handler()
# async def echo_upper(message: types.Message):
#     await message.answer(text=message.text.upper())

# Задача 2
@dp.message_handler()
async def check_two_words(message: types.Message):
    check = message.text
    check = check.split(' ')
    if len(check) >= 2:
        await message.answer(text=message.text)
    else:
        await message.answer(text="Как бы нужно сообщение с 2 слов")


# решение элегантнее message.text.count(' ') >= 1

if __name__ == '__main__':
    executor.start_polling(dp)