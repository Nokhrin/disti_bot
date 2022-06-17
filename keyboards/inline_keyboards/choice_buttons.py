from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline_keyboards.callbacks_data import recipes_callback

from data.config import URL_NASTOYKAS, URL_NALIVKAS
# recipes_drinks_choice - меню выбора рецепта напитка

## similar to regular keyboard - list of lists - like rows of buttons
# recipes_drinks_choice = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='Настойки', callback_data=recipes_callback.new(
#                 item_name='nastoykas_recipes'
#             )),
#             InlineKeyboardButton(text='Наливки', callback_data=recipes_callback.new(
#                 item_name='nalivkas_recipes'
#             )),
#             InlineKeyboardButton(text='Коктейли', callback_data=recipes_callback.new(
#                 item_name='cocktails_recipes'
#             )),
#         ],
#         [
#             InlineKeyboardButton(text='Отмена', callback_data='cancel'),
#         ],
#     ],
# )

# second method of creating keyboard
recipes_drinks_choice = InlineKeyboardMarkup(rowrow_width=2)
nastoykas_recipes = InlineKeyboardButton(text='Настойки', callback_data=recipes_callback.new(
                        item_name='nastoykas_recipes'
                    ))
recipes_drinks_choice.insert(nastoykas_recipes)

nalivkas_recipes = InlineKeyboardButton(text='Наливки', callback_data=recipes_callback.new(
                        item_name='nalivkas_recipes'
                    ))
recipes_drinks_choice.insert(nalivkas_recipes)

cocktails_recipes = InlineKeyboardButton(text='Коктейли', callback_data=recipes_callback.new(
                        item_name='cocktails_recipes'
                    ))
recipes_drinks_choice.insert(cocktails_recipes)

cancel_button = InlineKeyboardButton(text='Отмена', callback_data='cancel')
recipes_drinks_choice.insert(cancel_button)

# keyboard for nastoykas
kbd_nastoykas_recipes = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Смотреть рецепты настоек', url=URL_NASTOYKAS)
        ]
    ]
)

# keyboard for nalivkas
kbd_nalivkas_recipes = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Смотреть рецепты наливок', url=URL_NALIVKAS)
        ]
    ]
)
