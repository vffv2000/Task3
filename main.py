import logging

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

bot = Bot(token='5343231561:AAGB0nKpggD61U7t83sNgW_a0baKCQk2Deo')
dp = Dispatcher(bot)

# Импорт функций обработчиков из модулей
from start_commands import start_handler
from other_commands import help_handler, echo_handler

# Регистрация обработчиков команд
dp.register_message_handler(start_handler, commands=['start'])
dp.register_message_handler(help_handler, commands=['help'])
dp.register_message_handler(echo_handler)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)