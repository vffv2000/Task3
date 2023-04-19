from aiogram import types


async def help_handler(message: types.Message):
    await message.reply("Я могу понимать команды /start и /help")

async def echo_handler(message: types.Message):
    if message.text.lower() == 'привет':
        await message.reply('Приветствую!')
    elif message.text.lower() == 'пока':
        await message.reply('До свидания!')
    else:
        await message.reply('Не понимаю, что вы хотите.')