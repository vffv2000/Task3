# Импортируем необходимые библиотеки
import requests
from aiogram import types
import json

# Создаем пустой словарь payload и словарь headers с заголовком API-ключа
payload = {}
headers = {
  "apikey": "6YqPN8MyFR22HgPSafBTXA9TbhxgOG15"
}


# Обработчик команды /list_exchange
async def list_exchange_handler(message: types.Message):
    # URL для запроса списка доступных валют
    url = "https://api.apilayer.com/currency_data/list"
    # Выполняем GET-запрос с указанием URL, заголовков и пустого тела запроса
    response = requests.request("GET", url, headers=headers, data=payload)

    # Получаем код статуса и текст ответа
    status_code = response.status_code
    result = response.text

    # Разбиваем сообщение на более короткие сообщения, если оно слишком длинное
    if len(result) > 4096:
        message_parts = [result[i:i+4096] for i in range(0, len(result), 4096)]
        for part in message_parts:
            await message.reply(part)
    else:
        await message.reply(result)


# Обработчик команды /convert
async def convert_convert_handler(message: types.Message):
    # Извлекаем из сообщения параметры to, from и amount
    try:
        to = message.text.split()[1]
        fro = message.text.split()[2]
        amount = message.text.split()[3]
    except Exception as e:
        # Если параметры не указаны или указаны неверно, отправляем сообщение с инструкцией
        print("Exception (find):", e)
        await message.reply("Введите /convert СкакойВалюты ВКаккуюВалюту Кол-воВалюты")
        await message.reply("Если не знаете как обозначить валюты /list_ex")
        return

    try:
        # Составляем URL для запроса конвертации валют
        url = "https://api.apilayer.com/currency_data/convert?to={}&from={}&amount={}".format(to, fro, amount)

    except Exception as e:
        print("Exception (find):", e)
        await message.reply("Exception (find):", e)
        return
    # Выполняем GET-запрос с указанием URL, заголовков и пустого тела запроса
    response = requests.request("GET", url, headers=headers, data=payload)
    # Получаем код статуса и текст ответа
    status_code = response.status_code
    result = response.text
    # Отправляем сообщение с результатом конвертации
    await message.reply(
        f"Из {json.loads(result)['query']['amount']} {json.loads(result)['query']['from']}"
        f" мы получили {json.loads(result)['result']} {json.loads(result)['query']['to']}")
