# global objects
from aiogram import Bot, Dispatcher, types
from data import config

# initialize bot
bot = Bot(
        token=config.BOT_TOKEN,
        parse_mode=types.ParseMode.HTML
)
# for using on www.pythonanywhere.com with free account
# bot = Bot(token=bot_token, proxy=proxy_url)

dp = Dispatcher(bot)
