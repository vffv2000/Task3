from aiogram import types
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode


async def weather_handler(message: types.Message):

    s_city = message.text[9:]
    print(s_city)
    if s_city == "":
        await message.reply("Введите /weather Minsk или любой другой город")
        return
    city_id = 0
    appid = "4dbc9b8bce7411705a58d5a4a39c3186"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                            params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        city_id = data['list'][0]['id']
    except Exception as e:
        print("Exception (find):", e)
        await message.reply("Не удалось найти указанный город")
        return
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                            params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
        await message.reply("Город: " + str(data["name"]) + "\n" +
                             "Погодные условия: " + str(data['weather'][0]['description']) + "\n" +
                             "Температура за окном: " + str(data['main']['temp']) + "°C\n" +
                             "Ощущается как " + str(data["main"]["feels_like"]) + "°C",
                             parse_mode=ParseMode.HTML)
    except Exception as e:
        print("Exception (weather):", e)
        await message.reply("Не удалось получить данные о погоде для указанного города")