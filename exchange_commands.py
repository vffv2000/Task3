import requests
from aiogram import types
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
import json

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



async def convert_convert_handler(message: types.Message):
    #/convert to from amount
    try:
        to = message.text.split()[1]
        fro=message.text.split()[2]
        amount=message.text.split()[3]
    except Exception as e:
        print("Exception (find):", e)
        await message.reply("Введите /convert СкакойВалюты ВКаккуюВалюту Кол-воВалюты")
        await message.reply("Если не знаете как обозначить валюты /list_ex")
        return

    try:
        url = "https://api.apilayer.com/currency_data/convert?to={}&from={}&amount={}".format(to, fro, amount)

    except Exception as e:
        print("Exception (find):", e)
        await message.reply("Exception (find):", e)
        return
    response = requests.request("GET", url, headers=headers, data=payload)
    status_code = response.status_code
    result = response.text
    print(
        f"Из {json.loads(result)['query']['amount']} {json.loads(result)['query']['from']} мы получили {json.loads(result)['result']} {json.loads(result)['query']['to']}")

    await message.reply(
        f"Из {json.loads(result)['query']['amount']} {json.loads(result)['query']['from']} мы получили {json.loads(result)['result']} {json.loads(result)['query']['to']}")

