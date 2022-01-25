import config
from aiogram import Dispatcher, Bot


bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)
