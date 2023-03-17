"""
inline клавиатура
InlineKeyboardMarkup = row_width = int
InlineKeyboardButton = text = str = url = str = callback_data = str
"""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Button 1',
                           url='https://www.youtube.com/watch?v=WEVGU8qIJyM&ab_channel=PyLounge-%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%D0%BD%D0%B0Python%D0%B8%D0%B2%D1%81%D1%91%D0%BEIT')
ib2 = InlineKeyboardButton(text='Button 2',
                           url='https://hdrezka.ag/films/drama/52517-moy-uzhasnyy-sosed-2022.html')
ikb.add(ib1, ib2)


@dp.message_handler(commands=['start'])
async def send_kb(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Hello World!',
                           reply_markup=ikb)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)