from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


# Клавиатура главного меню
main_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Список команд')],
    [KeyboardButton(text='Отправить геолокацию')],
    [KeyboardButton(text='Контакты')]
], resize_keyboard=True)

# Клавиатура отправки геолокации
share_location = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Узнать погоду', request_location=True)],
    [KeyboardButton(text='Назад')]
], resize_keyboard=True)

# Клавиатура опций
inline_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Прогноз погоды на 1 день', callback_data='get_weather_one')],
    [InlineKeyboardButton(text="Прогноз погоды на 3 дня", callback_data="get_weather")],
    [InlineKeyboardButton(text="ГМЦ прогноз для одного города", callback_data="gmc_forecast")],
    [InlineKeyboardButton(text="ГМЦ прогноз для нескольких городов", callback_data="gmc_forecast_more")]
])
