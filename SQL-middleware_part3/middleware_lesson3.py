from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher.handler import CancelHandler #handler отмены обработки
from aiogram.dispatcher.middlewares import BaseMiddleware

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


ADMIN = 1630678041

class CustomMiddleware(BaseMiddleware):

    async def on_process_message(self, 
                                 message: types.Message, 
                                 data: dict):
        if message.from_user.id != ADMIN:
            raise CancelHandler()


@dp.message_handler(commands=['start']) #обработчик события message
async def cmd_start(message: types.Message) -> None:
    await message.reply('Ты написал команду старт!')

@dp.message_handler(lambda message: message.text.lower() == "привет")
async def text_hello(message: types.Message) -> None:    
    await message.reply('И тебе привет')

if __name__ == "__main__":
    dp.middleware.setup(CustomMiddleware())
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)