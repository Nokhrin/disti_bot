from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command, Text
from loader import dp
from keyboards.buttons_keyboards import keyboards_default_menu

@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer(
        'Выберите товар из меню ниже',
        reply_markup=keyboards_default_menu.menu
    )

@dp.message_handler(Text(equals=['Котлетки', 'Макарошки', 'Пюрешка']))
async def get_food(message: Message):
    await message.answer(
        f'Вы выбрали {message.text}.',
        reply_markup=ReplyKeyboardRemove()
    )
