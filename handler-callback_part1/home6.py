from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API, HELP_COMMAND

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Я запустился!')


@dp.message_handler(commands=["give"])
async def command_give(message: types.Message):
    await message.answer('Смотри какой милый кот❤️')
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEIHLRkDmS6et6BAaMfy7Rt8lEu5PUxAwACPyMAAia9MEqzjxYfl_2e1S8E')

@dp.message_handler(commands=["help"])
async def command_give(message: types.Message):
    await message.reply(text=HELP_COMMAND, parse_mode='HTML')

@dp.message_handler()
async def command_echo(message: types.Message):
    if message.text == '❤️':
        await message.answer('🖤')
    if '✅' in message.text:
        green = message.text.count('✅')
        await message.answer(green)

# Стикер id

@dp.message_handler(content_types=['sticker'])
async def send_stiker_id(message: types.message):
    await message.answer(message.sticker.file_id)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)