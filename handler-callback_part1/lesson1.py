from config import TOKEN_API
from aiogram import Bot, Dispatcher, executor, types

# бот - сервер, который будет взаимодейстовать с API Telegram.

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text) #написать сообщение


if __name__ == '__main__':
    executor.start_polling(dp)