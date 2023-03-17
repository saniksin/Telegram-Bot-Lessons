"""
CallbackQuery 
callback: types.CallbackQuery
"""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('❤️', callback_data='like'), InlineKeyboardButton('👎', callback_data='dislike')],
])


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message) -> None:
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://koshka.top/uploads/posts/2021-11/1637369753_1-koshka-top-p-ochen-smeshnogo-kota-1.jpg',
                         caption='Нравится ли тебе фотография?',
                         reply_markup=ikb)


@dp.callback_query_handler()
async def ikb_cb_handler(callback: types.CallbackQuery):
    print(callback)
    if callback.data == 'like':
        await callback.answer('Тебе понравилась фотография')
    await callback.answer('Тебе не понравилась фотография')


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, 
                           skip_updates=True)