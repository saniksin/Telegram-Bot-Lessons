from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
from config import TOKEN_API
import hashlib

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.inline_handler()
async def inline_cmd(inline_query: types.InlineQuery):
    text = inline_query.query or 'Empty'
    result_bold = hashlib.md5(text.encode()).hexdigest()
    text_italic = text + '1'
    result_italic = hashlib.md5(text_italic.encode()).hexdigest()


    item_bold = InlineQueryResultArticle(
        id=result_bold,
        input_message_content= InputTextMessageContent(f'<b>{text}</b>',parse_mode='HTML'),
        title = 'Bold',
        description='Empty',
        thumb_height=150,
        thumb_width=150,
        thumb_url = 'https://illustratorhow.com/wp-content/uploads/bold-text-illustrator7.png',
    )

    item_italic = InlineQueryResultArticle(
        id=result_italic,
        input_message_content=InputTextMessageContent(f'<em>{text}</em>', 
                                                      parse_mode='HTML'),
        title = 'Italic',
        description='Empty',
        thumb_height=150,
        thumb_width=150,
        thumb_url = 'https://cdn-icons-png.flaticon.com/512/59/59377.png',
    )

    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item_bold, item_italic],
                                  cache_time=1)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)