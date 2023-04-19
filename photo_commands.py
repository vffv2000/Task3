import requests
from aiogram import types


async def animal_handler(message: types.Message):    # определяем функцию-обработчик сообщений бота
    try:
        source = requests.get(f"https://random.dog/woof.json").text
        index = source.find("url")    # находим позицию, с которой начинается значение поля "url" в строке source
        await message.reply(source[index+6:-2])    # отправляем пользователю сообщение с изображением собаки, которое находится по ссылке в значении поля "url" в ответе сервера, обрезая при этом начало и конец строки source, чтобы получить только ссылку
    except Exception as e:
        print("Exception (find):", e)    # если произошла какая-то ошибка, выводим ее в консоль
        await message.reply("Временно не доступно")    # отправляем пользователю сообщение о том, что что-то пошло не так и сервис временно не доступен
        return    # выходим из функции
