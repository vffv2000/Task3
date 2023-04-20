from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создание объекта клавиатуры
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

# Создание кнопок и добавление их в клавиатуру
button1 = KeyboardButton('/help')
button2 = KeyboardButton('/weather')
button3 = KeyboardButton('convert')
button4 = KeyboardButton('/animal')


keyboard.add(button1, button2)
keyboard.add(button3, button4)

