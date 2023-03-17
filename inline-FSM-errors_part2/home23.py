from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton('❤️', callback_data='like'), InlineKeyboardButton('👎', callback_data='dislike')],
    [InlineKeyboardButton('Убрать фотографию и клавиатуру', callback_data='delete')]
])


like_flag = False
dislike_flag = False

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                        photo='https://koshka.top/uploads/posts/2021-11/1637369753_1-koshka-top-p-ochen-smeshnogo-kota-1.jpg',
                        caption='Нравится ли тебе эта фотография?',
                        reply_markup=ikb)

@dp.callback_query_handler()
async def ikb_cb_qh(callback: types.CallbackQuery):
    global like_flag
    global dislike_flag
    if callback.data == 'like':
        if like_flag != True:
            like_flag = True
            dislike_flag = False
            await callback.answer('Вам понравилась фотография')
        else:
            await callback.answer('Вы уже проголосовали')
    elif callback.data == 'dislike':
        if dislike_flag != True:
            like_flag = False
            dislike_flag = True
            await callback.answer('Вам не понравилась фотография')
        else:
            await callback.answer('Вы уже проголосовали')
    else:
        await callback.message.delete()
        

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)