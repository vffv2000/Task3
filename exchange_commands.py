import requests
from aiogram import types
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode

payload = {}
headers= {
  "apikey": "6YqPN8MyFR22HgPSafBTXA9TbhxgOG15"
}

async def list_exchange_handler(message: types.Message):
    url = "https://api.apilayer.com/currency_data/list"
    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text

    # Разбить сообщение на более короткие сообщения, если оно слишком длинное
    if len(result) > 4096:
        message_parts = [result[i:i+4096] for i in range(0, len(result), 4096)]
        for part in message_parts:
            await message.reply(part)
    else:
        await message.reply(result)


