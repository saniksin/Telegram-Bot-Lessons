"""
Inline Bot = инлайн режим Бота
BotFather

команда
/setinline
выбыраем бота
указываем тип сообщения 
в моем случае "Type a message..."

import aiogram InlineQueryResultArticle, InputTextMessageContent
import hashlib
"""

import hashlib
from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
from aiogram.utils.callback_data import CallbackData

from config import TOKEN_API

cb = CallbackData('ikb', 'action') #pattern
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

def get_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Button 1', callback_data=cb.new('push_1'))],
        [InlineKeyboardButton('Button 2', callback_data=cb.new('push_2'))]
    ])
    return ikb

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer(text='Какой-то текст для примера',
                         reply_markup=get_ikb())

@dp.callback_query_handler(cb.filter(action='push_1'))
async def cmd_cbqh(callback: types.CallbackQuery) -> None:
        await callback.answer('Hello')

@dp.callback_query_handler(cb.filter(action='push_2'))
async def cmd_cbqh(callback: types.CallbackQuery) -> None:
        await callback.answer('World')


#inline handlers

@dp.inline_handler()
async def inline_echo(inline_query: types.InlineQuery) -> None:
    text = inline_query.query or 'Not any text' #получили текст от пользователя
    input_content = InputTextMessageContent(text) #формируем контент ответного сообщения
    result_id = hashlib.md5(text.encode()).hexdigest() #сделали уникальный ID результата
    print(result_id)

    item = InlineQueryResultArticle(
         input_message_content=input_content,
         id=result_id,
         title='Echo!!!'
    )

    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item],
                                  cache_time=1)

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)