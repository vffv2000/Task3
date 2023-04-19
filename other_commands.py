from aiogram import types


async def help_handler(message: types.Message):
    await message.reply("Я могу понимать команды /start и /help")

