from aiogram import types
from loader import dp

# start command handler
@dp.message_handler(commands=['start'])
async def get_start(message: types.Message):
    await bot.send_message(
            message.from_user.id,
            f'Здравствуйте, {message.from_user.first_name}.\nДоступны команды\n/menu\n/help\n/about'
        )
