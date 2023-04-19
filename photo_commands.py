import requests
from aiogram import types


async def animal_handler(message: types.Message):
    try:
        source = requests.get(f"https://random.dog/woof.json").text
        index=source.find("url")
        await message.reply(source[index+6:-2])
    except Exception as e:
        print("Exception (find):", e)
        await message.reply("Временно не доступно")
        return




