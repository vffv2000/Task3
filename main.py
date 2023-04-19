import logging
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from start_commands import start_handler
from other_commands import help_handler, echo_handler

logging.basicConfig(level=logging.INFO)

bot = Bot(token='5343231561:AAGB0nKpggD61U7t83sNgW_a0baKCQk2Deo')
dp = Dispatcher(bot)
dp.register_message_handler(start_handler, commands=['start'])
dp.register_message_handler(help_handler, commands=['help'])
dp.register_message_handler(echo_handler)


async def on_startup(dp):
    await bot.send_message(chat_id='556907227', text='Бот запущен')

async def on_shutdown(dp):
    await bot.send_message(chat_id='556907227', text='Бот остановлен')

async def main():
    # Регистрация обработчиков команд
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(help_handler, commands=['help'])
    dp.register_message_handler(echo_handler)

    # Запуск бота
    await dp.start_polling(on_startup=on_startup, on_shutdown=on_shutdown)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
