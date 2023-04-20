from aiogram import types


async def help_handler(message: types.Message):
    reply_text = "Привет! Я могу выполнить следующие команды:\n"
    reply_text += "/start - запустить бота и получить приветственное сообщение\n"
    reply_text += "/help - получить справочную информацию о командах бота\n"
    reply_text += "/animal - получить случайное фото животного\n"
    reply_text += "/convert - конвертировать валюту (например: /convert USD EUR 100)\n"
    reply_text += "/list_ex - получить список доступных валют для конвертации\n"
    reply_text += "/weather - получить прогноз погоды для указанного города (например: /weather Moscow)"

    await message.reply(reply_text)
