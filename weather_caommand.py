from aiogram import types
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode

# Обработчик команды /weather
async def weather_handler(message: types.Message):
    try:
        s_city = message.text.split()[1] # Получаем название города из сообщения пользователя
    except Exception as e:
        print("Exception (find):", e)
        await message.reply("Введите /weather Название_города")
        return
    print(s_city)

    # Получаем данные о погоде из OpenWeatherMap API
    appid = "4dbc9b8bce7411705a58d5a4a39c3186"
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                            params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        city_id = data['list'][0]['id'] # Получаем ID города для использования в следующем запросе
    except Exception as e:
        print("Exception (find):", e)
        await message.reply("Не удалось найти указанный город")
        return

    # Получаем данные о погоде для указанного города
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                            params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()

        # Отправляем сообщение пользователю с данными о погоде
        await message.reply("Город: " + str(data["name"]) + "\n" +
                             "Погодные условия: " + str(data['weather'][0]['description']) + "\n" +
                             "Температура за окном: " + str(data['main']['temp']) + "°C\n" +
                             "Ощущается как " + str(data["main"]["feels_like"]) + "°C",
                             parse_mode=ParseMode.HTML)
    except Exception as e:
        print("Exception (weather):", e)
        await message.reply("Не удалось получить данные о погоде для указанного города")
