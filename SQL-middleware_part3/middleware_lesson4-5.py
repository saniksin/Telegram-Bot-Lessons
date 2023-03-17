"""
Декоратор с динамической функцией который поможет устанавливать права для пользователей
"""

from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher.handler import CancelHandler, current_handler #handler отмены обработки
from aiogram.dispatcher.middlewares import BaseMiddleware

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


def set_key(key: str = None):
    
    def decorator(func):
        setattr(func, 'key', key)

        return func
    
    return decorator


class AdminMiddleware(BaseMiddleware):

    async def on_process_message(self, message: types.Message, data: dict) -> None:

        handler = current_handler.get()

        if handler:
            key = getattr(handler, 'key', 'Такого атрибута нет')
            print(key)


@dp.message_handler(commands=['start']) #обработчик события message
async def cmd_start(message: types.Message) -> None:
    await message.reply('Ты написал команду старт!')

@dp.message_handler(lambda message: message.text.lower() == "привет")
@set_key('hello!')
async def text_hello(message: types.Message) -> None:    
    await message.reply('И тебе привет')

if __name__ == "__main__":
    dp.middleware.setup(AdminMiddleware())
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)