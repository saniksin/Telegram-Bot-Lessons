from aiogram import executor
from router import dp

async def on_startup(_):
    print('Я успешно запустился и пропустил все объявления!')

if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)