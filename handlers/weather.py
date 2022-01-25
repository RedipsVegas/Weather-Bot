from aiogram import types
import flag
from common import dp
from services import weather_api
from database.query import insert_user


@dp.message_handler(commands=['start'])
async def user(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_name = message.from_user.username
    city = message.text
    await insert_user(first_name, last_name, user_name, city)


@dp.message_handler()
async def weather(message: types.Message):
    status, body = await weather_api.get_weather(city=message.text)
    if status != 200:
        await message.answer(f'City {message.text} not found!')
        return
    text = (f'City: {body["name"]}{flag.flag(body["sys"]["country"])}\n'
            f'Temp: {int(body["main"]["temp"]) - 273}°C\n'
            f'Feels like: {int(body["main"]["feels_like"]) - 273}°C\n'
            f'Humidity: {body["main"]["humidity"]}%'
            )
    await message.answer(text)
