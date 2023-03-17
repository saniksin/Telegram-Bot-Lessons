"""
pre-process update
process update 
pre-process message|callback_query
filter(lambda message: not message.photo)
process message|callback_query|...
handler
post process message
post process update
"""

from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher.middlewares import BaseMiddleware

from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

class CustomMiddleware(BaseMiddleware):

    async def on_pre_process_update(self, update: types.Update, data: dict):
        #print('It works! PRE PROCESS UPDATE')
        pass

    async def on_process_update(self, update: types.Update, data: dict):
        #print('It works! PROCESS UPDATE')
        pass

    async def on_process_message(self, message: types.Message, data: dict):
        print(data, message)

@dp.message_handler(commands=['start']) #обработчик события message
async def cmd_start(message: types.Message) -> None:
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton('Test',callback_data='data_test')]
    ])
    await message.reply('Ты написал команду старт!',
                        reply_markup=ikb)
    print('World')


if __name__ == "__main__":
    dp.middleware.setup(CustomMiddleware())
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)