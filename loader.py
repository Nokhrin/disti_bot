# global objects
from aiogram import Bot, Dispatcher, executor, types
from data import config

consts = config.load_consts('.ini')

# initialize bot
bot = Bot(
        token=consts.bot_token,
        parse_mode=types.ParseMode
        )
# for using on www.pythonanywhere.com with free account
# bot = Bot(token=bot_token, proxy=proxy_url)

dp = Dispatcher(bot)
