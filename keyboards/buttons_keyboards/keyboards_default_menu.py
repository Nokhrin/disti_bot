from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# keyboard markup
# each list in "keyboard" list is row of buttons
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Котлетки'),
        ],
        [
            KeyboardButton(text='Макарошки'),
            KeyboardButton(text='Пюрешка'),
        ],
    ],
    resize_keyboard=True
)
