"""
callback функция
callback_query:
id: str
from: user
message: Message()
data: str

callback: types.CallbackQuery
callback_query_handler
"""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN_API, HELP_COMMAND

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('I have been started up')


kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='/help')
b2 = KeyboardButton(text='/vote')
kb.add(b1, b2)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Welcome to our bot!",
                           reply_markup=kb)

@dp.message_handler(commands=['vote'])
async def vote_command(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text='❤️',
                               callback_data='like')
    ib2 = InlineKeyboardButton(text='👎',
                               callback_data='dislike')
    ikb.add(ib1, ib2)

    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://prophotos.ru/data/articles/0002/2622/image-rectangle_600_x.jpg',
                         caption='Нравится ли тебе эта фотография?',
                         reply_markup=ikb)


@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    print(callback)
    if callback.data == 'like':
        await callback.answer(text='Тебе понравилась данная фотография!')
    await callback.answer('Тебе не понравилась эта фотография!')


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, 
                           skip_updates=True,
                           on_startup=on_startup)