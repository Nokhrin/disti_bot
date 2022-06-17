# bot (app) runner

# import keyboard_markups
import logging

# from aiogram.types import ReplyKeyboardRemove

from aiogram import executor # to start polling
from loader import dp
import handlers
from helpers.admin_utils.notify_admin import send_to_admin
from helpers.admin_utils.set_bot_commands import set_commands_info

async def run_on_startup(dispatcher):
    # set default commands description
    await set_commands_info(dispatcher)
    # send message aboot starting bot
    await send_to_admin(dispatcher)


# start bot
def main():
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=run_on_startup
    )

if __name__ == '__main__':
    main()
