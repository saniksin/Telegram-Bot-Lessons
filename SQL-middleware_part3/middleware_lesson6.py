"""
кто создал кнопку тот и нажимает, проверка.
"""

from aiogram import types, executor, Dispatcher, Bot
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware 

from config import TOKEN_API

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot=bot)


class CheckMiddleware(BaseMiddleware):

    async def on_process_callback_query(self, callback: types.CallbackQuery, dict: dict):
        
        callback_id = callback.data[callback.data.find('_')+1:]

        if callback_id != str(callback.from_user.id):

            raise CancelHandler()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    ikb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton('Тестовая кнопка!', callback_data=f'check_{message.from_user.id}')]
    ])
    await message.answer('Текстовое сообщение',
                         reply_markup=ikb)


@dp.callback_query_handler(lambda callback: callback.data.startswith('check_'))
async def cmd_button_answer(callback: types.CallbackQuery):
    await callback.message.answer('Ты нажал на свою кнопку!')

if __name__ == "__main__":
    dp.middleware.setup(CheckMiddleware())
    executor.start_polling(skip_updates=True,
                           dispatcher=dp)