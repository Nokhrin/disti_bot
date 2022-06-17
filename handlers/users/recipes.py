# handler for recipes


from aiogram.types import Message, CallbackQuery
# commands filter
from aiogram.dispatcher.filters import Command
from keyboards.inline_keyboards.choice_buttons import recipes_drinks_choice, kbd_nastoykas_recipes, kbd_nalivkas_recipes

from helpers.logging_setup import logging_setup
from keyboards.inline_keyboards.callbacks_data import recipes_callback

# importing dispatcher, which is already imported by loader.py
from loader import dp, bot

@dp.message_handler(Command('recipes'))
async def show_recipes(message: Message):
    await message.answer(
        text=f'Знаю рецепты наливок, настоек, коктейлей.\nЕсли передумали, жмите \"отмена\"',
        reply_markup=recipes_drinks_choice
    )

# TODO - send russian name in callback

# handler for callback queries
# using filter to catch callbacks by item_name
# filters should go in the order from general to specific
@dp.callback_query_handler(recipes_callback.filter(item_name='nalivkas_recipes'))
# filter will return a dictionary
async def get_nalivkas_recipes(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=30)
    logging_setup.logging.info(f'callback content: {callback_data}')
    item_name = callback_data.get('item_name')
    await call.message.answer('Вы выбрали рецепты наливок', reply_markup=kbd_nalivkas_recipes)

# built-in filter of aiogram - text_contains
@dp.callback_query_handler(text_contains='nastoykas')
async def get_nastoykas_recipes(call: CallbackQuery):
    # hard approach
    #await bot.answer_callback_query(callback_query_id=call.id)
    # simple approach
    await call.answer(cache_time=30) # hide clock, set waiting time for next code to run
    # check contents of callback
    callback_data = call.data
    logging_setup.logging.info(f'callback content: {callback_data}')
    await call.message.answer('Вы выбрали рецепты настоек', reply_markup=kbd_nastoykas_recipes)

# cancel button
@dp.callback_query_handler(text_contains='cancel')
async def send_cancel(call: CallbackQuery):
    callback_data = call.data
    logging_setup.logging.info(f'callback content: {callback_data}')
    await call.answer('Вы отменили выбор', show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)
