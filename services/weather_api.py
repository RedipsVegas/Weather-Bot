from functools import partial
import aiohttp
from config import WEATHER_API_TOKEN
import typing


API_URL: str = 'http://api.openweathermap.org/data/2.5/'

api_session = aiohttp.ClientSession()


async def weather_api_call(*_, session: aiohttp.ClientSession = api_session, api_url: str = API_URL,
                           token: str = WEATHER_API_TOKEN, collection: str, city: str) -> tuple[int, typing.Any]:
    url = f"{api_url}{collection}?q={city}&appid={token}"
    async with session.get(url) as response:
        return response.status, await response.json()


get_weather = partial(weather_api_call, collection='weather')
get_forecast = partial(weather_api_call, collection= 'forecast')
