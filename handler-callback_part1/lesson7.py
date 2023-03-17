"""
Отправка фото
Отправка локации
Отправка в чат essage.chat.id
Отправка локации
skip_updates
"""

from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API, HELP_COMMAND

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['картинка'])
async def send_photo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://img.freepik.com/free-photo/landscape-of-morning-fog-and-mountains-with-hot-air-balloons-at-sunrise_335224-794.jpg")
    await message.delete()


@dp.message_handler(commands=['location'])
async def send_point(message: types.Message):
    await bot.send_location(chat_id=message.chat.id,
                            latitude=51.085907,
                            longitude=17.009242)
    await message.delete()


@dp.message_handler()
async def help_command(message: types.Message):
    # await message.answer(message.text)
    # await bot.send_message(chat_id=message.from_user.id,
    #                       text="Hello")
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode="HTML")
    await message.delete()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)