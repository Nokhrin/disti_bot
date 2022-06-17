# set commands description on bot start

from aiogram import types

async def set_commands_info(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'начать работу'),
            types.BotCommand('menu', 'все инструменты'),
            types.BotCommand('help', 'как пользоваться'),
            types.BotCommand('about', 'контакт для предложений и замечаний'),
        ]
    )
