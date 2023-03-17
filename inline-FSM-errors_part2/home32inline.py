from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent
from config import TOKEN_API
import hashlib

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

@dp.inline_handler()
async def cmd_inline_text(inline_query: types.InlineQuery):
    if inline_query.query.lower() == 'photo':
        text = 'This is a photo'
    else:
        text = inline_query.query or 'Echo'
    input_content = InputTextMessageContent(text)
    id_result = hashlib.md5(text.encode()).hexdigest()

    item = InlineQueryResultArticle(
        id=id_result,
        title=text,
        input_message_content=input_content
    )

    await bot.answer_inline_query(inline_query_id=inline_query.id,
                                  results=[item],
                                  cache_time=1)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True)