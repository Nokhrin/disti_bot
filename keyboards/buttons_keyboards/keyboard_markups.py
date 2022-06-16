from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# go back to main menu
btn_back_to_main = KeyboardButton(f'Главное меню')
# go back to calculators
btn_back_to_calculators = KeyboardButton(f'Назад к Калькуляторам')


### main menu ###
## buttons
btn_calculators = KeyboardButton(f'Калькуляторы')
btn_recipes = KeyboardButton(f'Рецепты')
btn_info = KeyboardButton(f'Информация')
btn_close_menu = KeyboardButton(f'Закрыть меню')
## keyboard layout
kbd_main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(
        btn_calculators,
        btn_recipes,
        btn_info,
        btn_close_menu
    )

### calculators menu ###
## buttons

#-- разбавление - основное меню
btn_dilution = KeyboardButton(f'Разбавление')

#- разбавление - подменю
btn_water_volume = KeyboardButton(f'Расчёт воды по крепости')
btn_fertman = KeyboardButton(f'Расчет по Фертману')
btn_fertman_classic = KeyboardButton(f'Таблица Фертмана')
btn_alcoholic_solutions_mix = KeyboardButton(f'Смешение спиртовых растворов')
btn_alcoholic_solutions_dilution = KeyboardButton(f'Разбавление спиртовых растворов')
# btn_back_to_dilution = KeyboardButton(f'назад к Разбавлению')

# разбавление - keyboard layout
kbd_dilution = ReplyKeyboardMarkup(resize_keyboard=True).add(
    btn_water_volume,
    btn_fertman,
    btn_fertman_classic,
    btn_alcoholic_solutions_mix,
    btn_alcoholic_solutions_dilution,
    btn_back_to_calculators,
    )

#-- отбор - основное меню
btn_selection = KeyboardButton(f'Отбор')
#- отбор - подменю
btn_heads_hearts_tails = KeyboardButton(f'Расчет голов, тела, хвостов')
btn_temperature_correction = KeyboardButton(f'Коррекция крепости по температуре')
# btn_back_to_selection = KeyboardButton(f'назад к Отбору')

# отбор - keyboard layout
kbd_selection = ReplyKeyboardMarkup(resize_keyboard=True).add(
    btn_heads_hearts_tails,
    btn_temperature_correction,
    btn_back_to_calculators,
    )

#-- брага и заторы - основное меню
btn_wash = KeyboardButton(f'Брага и заторы')
#- брага и заторы - подменю
btn_sugar_by_yeast = KeyboardButton(f'Количество сахара по толерантности')
btn_sugar_wash_volume = KeyboardButton(f'Объём сахарной браги')
btn_wash_measurement = KeyboardButton(f'Измерение сусла')
btn_sugar_wash_calculation = KeyboardButton(f'Расчёт сахарной браги')
btn_grain_wash_calculation = KeyboardButton(f'Расчёт зерновой браги')
btn_back_to_wash = KeyboardButton(f'назад к Браге и затору')

# брага и заторы - keyboard layout
kbd_wash = ReplyKeyboardMarkup(resize_keyboard=True).add(
    btn_sugar_by_yeast,
    btn_sugar_wash_volume,
    btn_wash_measurement,
    btn_sugar_wash_calculation,
    btn_grain_wash_calculation,
    btn_back_to_calculators,
    )

## keyboard layout - calculators
kbd_calculators = ReplyKeyboardMarkup(resize_keyboard=True).add(
    btn_dilution,
    btn_selection,
    btn_wash,
    btn_back_to_main,
    )


#################################
### recipes menu ###
## buttons

#-- рецепты - основное меню
# btn_recipes = KeyboardButton(f'Рецепты')

#- рецепты - подменю
btn_wash_recipes = KeyboardButton(f'Браги и заторы')
btn_drink_recipes = KeyboardButton(f'Напитки')
btn_food_recipes = KeyboardButton(f'Еда')

## рецепты - keyboard layout
kbd_recipes = ReplyKeyboardMarkup(resize_keyboard=True).add(
    btn_wash_recipes,
    btn_drink_recipes,
    btn_food_recipes,
    btn_back_to_main,
    )



#################################
### information menu ###
## buttons

#-- информация - основное меню
# btn_info = KeyboardButton(f'Рецепты')

#- информация - подменю
btn_hints_and_tips = KeyboardButton(f'Полезные советы')
btn_contacts = KeyboardButton(f'Контакты')
btn_about = KeyboardButton(f'О боте')

## информация - keyboard layout
kbd_information = ReplyKeyboardMarkup(resize_keyboard=True).add(
    btn_hints_and_tips,
    btn_contacts,
    btn_about,
    btn_back_to_main,
    )
