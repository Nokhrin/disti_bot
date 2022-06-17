# store callbacks separately from keyboard markups for convenience

from aiogram.utils.callback_data import CallbackData

# recipes_callback = CallbackData('command', 'item_name', 'quantity')

recipes_callback = CallbackData('recipes_drinks', 'item_name')
