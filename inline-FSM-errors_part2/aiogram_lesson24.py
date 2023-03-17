"""
Callback data count
"""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

number = 0

def get_inline_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Increase', callback_data='btn_increase'), InlineKeyboardButton('Decrease', callback_data='btn_decrease')],
    ])
    return ikb


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer(f'The current number is {number}',
                         reply_markup=get_inline_keyboard())

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith('btn'))
async def ikb_cb_handler(callback: types.CallbackQuery) -> None:
    global number
    if callback.data == 'btn_increase':
        number += 1
        await callback.message.edit_text(f'The current number is {number}',
                                         reply_markup=get_inline_keyboard())
    if callback.data == 'btn_decrease':
        number -= 1
        await callback.message.edit_text(f'The current number is {number}',
                                         reply_markup=get_inline_keyboard())

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)