from aiogram import types


class PollMachine:
    def __init__(self):
        self.states = {
            "start": self.start,
            "get_topic": self.get_topic,
            "get_options": self.get_options,
            "finish": self.finish,
        }
        self.poll = {}

    async def start(self, message: types.Message):
        self.poll = {}
        await message.answer("Добро пожаловать в мастер создания опросов! Какую тему вы хотите выбрать?")
        return "get_topic"

    async def get_topic(self, message: types.Message):
        self.poll["topic"] = message.text
        await message.answer(f"Тема опроса: {self.poll['topic']}. Сколько вариантов ответов нужно?")
        return "get_options"

    async def get_options(self, message: types.Message):
        try:
            num_options = int(message.text)
            self.poll["options"] = num_options
            await message.answer("Введите варианты ответов через запятую.")
            return "finish"
        except ValueError:
            await message.answer("Некорректный ввод. Пожалуйста, введите число.")
            return "get_options"

    async def finish(self, message: types.Message):
        options = message.text.split(",")
        options = [o.strip() for o in options]
        self.poll["answers"] = options
        await message.answer("Опрос создан!")
        # отправляем опрос в вашу базу данных или в какой-то другой сервис
        print(self.poll)
        return "start"
