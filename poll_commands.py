from aiogram import types

from poll_machine import PollMachine

poll_machine = PollMachine()

async def create_poll_handler(message: types.Message):
    current_state = "start"
    while current_state is not None:
        current_state = await poll_machine.states[current_state](message)
