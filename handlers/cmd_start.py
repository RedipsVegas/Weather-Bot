from aiogram import types
from common import dp


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Hey, I'm worst weather bot."
                         "Send city name for current weather or forecast")
