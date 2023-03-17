from aiogram import types
from keyboards import kb, ikb
from configs import HELP_COMMAND, PHOTO_LIST, STIKERS_LIST
from bot import bot
import random

async def command_start(message: types.Message):
    await message.answer(text='Добро пожаловать! Выберите опцию',
                         reply_markup=kb)

async def command_help(message: types.Message):
    await message.answer(text=HELP_COMMAND,
                         parse_mode="HTML")

async def command_description(message: types.Message):
    await message.reply(text="Наш бот высылает рандомные фотографии, стикеры и координаты завода!")

async def command_random(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random.choice(PHOTO_LIST),
                         caption="Прикольное фото!",
                         reply_markup=ikb)

async def callback_data_command(callback: types.CallbackQuery):
    message = callback['message']
    if callback.data == 'next':
        await callback.answer('Следующая фотография!')
        await command_random(message)
    elif callback.data == 'like':
        await callback.answer('Вам понравилась фотография')
    elif callback.data == 'dislike':
        await callback.answer('Вам не понравилась фотография')
    if callback.data == 'start':
        await command_start(message)
        await callback.answer('Вы вернулись в главное меню!')
    
async def command_stickers(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker=random.choice(STIKERS_LIST))
    
async def command_location(message: types.Message):
    await message.reply(text='Высылаю тебе кординаты завода!')
    await bot.send_location(chat_id=message.chat.id,
                            latitude=51.0227006,
                            longitude=16.889638)

async def command_emoji(message: types.Message):
    await message.reply(text='Я не нашел такой команды, попробуй еще раз...❤️')
    
