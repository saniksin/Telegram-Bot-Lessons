"""
ТЕМА:
1. on_startup
2. parse_mode = "HTML"
3. emoji, stickers
4. on_shutdown

"""

from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

# Сообщение при запуске
async def on_startup(_):
    print('Бот был успешно запущен!')
# Сообщение при завершение
async def on_shutdown(_):
    print('Бот был успешно закрыт')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='<em>Привет, <b>добро пожаловать</b> в наш БОТ!</em>', 
                         parse_mode="HTML")

@dp.message_handler(commands=['give'])
async def give_command(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEIHLRkDmS6et6BAaMfy7Rt8lEu5PUxAwACPyMAAia9MEqzjxYfl_2e1S8E")
    await message.delete()


@dp.message_handler()
async def echo_command(message: types.Message):
    await message.answer(text=f'{message.text}  ❤️')
    await message.delete()

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)