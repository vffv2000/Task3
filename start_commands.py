from aiogram import types
from buttons import *

async def start_handler(message: types.Message):
    # Отправка сообщения с клавиатурой
    await message.answer("Выберите команду:", reply_markup=keyboard)
    await message.reply("Привет!")
