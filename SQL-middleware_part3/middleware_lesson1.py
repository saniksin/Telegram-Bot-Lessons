from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher.middlewares import BaseMiddleware

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

class TestMiddleWare(BaseMiddleware):

    async def on_process_update(self, update, data):
        print('Более высокий слой пирога')
        print(update)
        print(data)

    async def on_pre_process_update(self, update: types.Update, data: dict):
        print('Hello')
        print(update)
        print(data)

@dp.message_handler(commands=['start']) #обработчик события message
async def cmd_start(message: types.Message) -> None:
    await message.reply('Ты написал команду старт!')
    print('World')


if __name__ == "__main__":
    dp.middleware.setup(TestMiddleWare()) #регистрируем middleware
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)