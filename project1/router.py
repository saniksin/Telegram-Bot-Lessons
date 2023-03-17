from bot import dp
import handlers as hs

dp.register_message_handler(hs.command_start, commands=['start'])
dp.register_message_handler(hs.command_help, commands=['help'])
dp.register_message_handler(hs.command_description, commands=['description'])
dp.register_message_handler(hs.command_random, commands=['random'])
dp.register_message_handler(hs.command_stickers, commands=['sticker'])
dp.register_message_handler(hs.command_location, commands=['location'])
dp.register_message_handler(hs.command_emoji)
dp.register_callback_query_handler(hs.callback_data_command)