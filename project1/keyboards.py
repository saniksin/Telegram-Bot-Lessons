from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton('/help')
button_2 = KeyboardButton('/description')
button_3 = KeyboardButton('/random')
button_4 = KeyboardButton('/sticker')
button_5 = KeyboardButton('/location')
kb.add(button_1, button_2).add(button_3, button_4, button_5)

ikb = InlineKeyboardMarkup(row_width=3)
button1 = InlineKeyboardButton(text='Следующая фотография',
                               callback_data='next')
button2 = InlineKeyboardButton(text='👍',
                               callback_data='like')
button3 = InlineKeyboardButton(text='👎',
                               callback_data='dislike')
button4 = InlineKeyboardButton(text='Переход в главное меню',
                               callback_data='start')
 
ikb.add(button1).add(button2, button3).add(button4)

