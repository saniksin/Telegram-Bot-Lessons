from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup 

ikb = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text="Ссылка 1",
                          url='https://chat.openai.com/chat')
b2 = InlineKeyboardButton(text='Ссылка 2',
                          url='https://www.google.com/search?q=funny+cats&sxsrf=AJOqlzV4S4uSp7wC8bsoll1RIojBIGsAfQ:1678721180837&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj5pKTdm9n9AhUuCBAIHQZtDaYQ_AUoAXoECAEQAw&biw=998&bih=949&dpr=1#imgrc=E9qn7ng6xkALTM')

ikb.add(b1).insert(b2)