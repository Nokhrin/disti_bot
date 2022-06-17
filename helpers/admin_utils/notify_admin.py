import logging
from aiogram import Dispatcher
from data.config import ADMIN_ID

async def send_to_admin(dp: Dispatcher):
    try:
        await dp.bot.send_message(
                        chat_id=ADMIN_ID,
                        text='Bot has been started'
        )
    except Exception as err:
        logging.exception(err)
