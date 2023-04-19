import logging

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Установка уровня логирования
logging.basicConfig(level=logging.INFO)

# Создание экземпляра бота
bot = Bot(token='5343231561:AAGB0nKpggD61U7t83sNgW_a0baKCQk2Deo')

# Создание диспетчера
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!")

# Обработчик команды /help
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Я могу понимать команды /start и /help")

# Обработчик текстовых сообщений
@dp.message_handler()
async def echo_message(msg: types.Message):
    if msg.text.lower() == 'привет':
        await msg.reply('Приветствую!')
    elif msg.text.lower() == 'пока':
        await msg.reply('До свидания!')
    else:
        await msg.reply('Не понимаю, что вы хотите.')

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
