# bot (app) runner

# import keyboard_markups
import logging
# # from aiogram import Bot, Dispatcher, executor, types
# import config
# from config import bot_token, proxy_url

from aiogram.types import ReplyKeyboardRemove

from aiogram import executor
from loader import dp
import handlers
from helpers.notify_admin import send_to_admin
from helpers.set_bot_commands import set_commands_info
from data.config import load_consts

async def run_on_startup(dispatcher):
    # set default commands description
    await set_commands_info(dispatcher)
    # send message aboot starting bot
    await send_to_admin(dispatcher)



# logging.basicConfig(filename=config.log_path,
#                     filemode=config.log_filemode,
#                     encoding=config.log_encoding,
#                     format=config.log_format,
#                     level=config.log_level)

# initialize bot
# bot = Bot(token=bot_token)
# for using on www.pythonanywhere.com with free account
# bot = Bot(token=bot_token, proxy=proxy_url)

# dp = Dispatcher(bot)

# # start command
# @dp.message_handler(commands=['start'])
# async def get_start(message: types.Message):
#     if message.chat.type == 'private':
#         # logging.info(message) # for checking out message attributes
#         await bot.send_message(
#                 message.from_user.id,
#                 f'Здравствуйте, {message.from_user.first_name}.\nДоступны команды\n/menu\n/help\n/about',
#                 reply_markup=ReplyKeyboardRemove()
#             )

# help command
@dp.message_handler(commands=['help'])
async def get_help(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(
                message.from_user.id,
                f'Нажмите /menu, чтобы перейти к инструментам.',
                reply_markup=ReplyKeyboardRemove()
            )

# about command
@dp.message_handler(commands=['about'])
async def get_about(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(
                message.from_user.id,
                f'Разработчик @nohal\nПишите, что добавить или исправить в работе бота.',
                reply_markup=ReplyKeyboardRemove()
            )

#######################
### menu
##
@dp.message_handler(commands=['menu', 'меню'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        # logging.info(message) # for checking out message attributes
        await bot.send_message(
                message.from_user.id,
                f'Главное меню',
                reply_markup=keyboard_markups.kbd_main_menu
            )

# listen to keyboard
@dp.message_handler()
async def open_main_menu(message: types.Message):
    if message.chat.type == 'private':
        # preparing text of message to make it convenient to work with
        message_text_prepared = message.text.lower()
        # check commands from buttons
        if message_text_prepared == 'главное меню':
            await bot.send_message(
                message.from_user.id,
                f'Главное меню',
                reply_markup=keyboard_markups.kbd_main_menu
            )
        elif message_text_prepared in ['калькуляторы', 'назад к калькуляторам']:
            await bot.send_message(
                message.from_user.id,
                f'Калькуляторы',
                reply_markup=keyboard_markups.kbd_calculators,
            )
        elif message_text_prepared == 'рецепты':
            await bot.send_message(
                message.from_user.id,
                f'Рецепты',
                reply_markup=keyboard_markups.kbd_recipes,
            )
        elif message_text_prepared == 'информация':
            await bot.send_message(
                message.from_user.id,
                f'Информация',
                reply_markup=keyboard_markups.kbd_information,
            )

        ### разбавление - dilution submenu
        elif message_text_prepared == 'разбавление':
            await bot.send_message(
                message.from_user.id,
                f'Разбавление',
                reply_markup=keyboard_markups.kbd_dilution,
            )
        # elif message_text_prepared == 'информация':
        #     await bot.send_message(
        #         message.from_user.id, f'Информация',
        #         reply_markup=keyboard_markups.kbd_information,
        #     )
        # elif message_text_prepared == 'информация':
        #     await bot.send_message(
        #         message.from_user.id, f'Информация',
        #         reply_markup=keyboard_markups.kbd_information,
        #     )
        # elif message_text_prepared == 'информация':
        #     await bot.send_message(
        #         message.from_user.id, f'Информация',
        #         reply_markup=keyboard_markups.kbd_information,
        #     )


        ### отбор - selection submenu
        elif message_text_prepared in ['отбор', 'назад к отбору']:
            await bot.send_message(
                message.from_user.id,
                f'Отбор',
                reply_markup=keyboard_markups.kbd_selection,
            )
        # elif message_text_prepared == 'информация':
        #     await bot.send_message(
        #         message.from_user.id, f'Информация',
        #         reply_markup=keyboard_markups.kbd_information,
        #     )
        # elif message_text_prepared == 'информация':
        #     await bot.send_message(
        #         message.from_user.id, f'Информация',
        #         reply_markup=keyboard_markups.kbd_information,
        #     )
        # elif message_text_prepared == 'информация':
        #     await bot.send_message(
        #         message.from_user.id, f'Информация',
        #         reply_markup=keyboard_markups.kbd_information,
        #     )


        ### брага и заторы - wash submenu
        elif message_text_prepared in ['брага и заторы', 'назад к браге и заторам']:
            await bot.send_message(
                message.from_user.id,
                f'Брага и заторы',
                reply_markup=keyboard_markups.kbd_wash,
            )
        # elif message_text_prepared == 'информация':
        #     await bot.send_message(
        #         message.from_user.id, f'Информация',
        #         reply_markup=keyboard_markups.kbd_information,
        #     )
        # elif message_text_prepared == 'информация':
        #     await bot.send_message(
        #         message.from_user.id, f'Информация',
        #         reply_markup=keyboard_markups.kbd_information,
        #     )
        # elif message_text_prepared == 'информация':
        #     await bot.send_message(
        #         message.from_user.id, f'Информация',
        #         reply_markup=keyboard_markups.kbd_information,
        #     )

        # hide buttons
        elif message_text_prepared in ['закрыть меню']:
            await bot.send_message(
                message.from_user.id,
                f'Закрыл меню',
                reply_markup=ReplyKeyboardRemove(),
            )

        else:
            await message.reply(
                f'Извините, не понимаю вашу команду'
            )


# start bot
def main():
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
        on_startup=run_on_startup
    )

if __name__ == '__main__':
    main()
