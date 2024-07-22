from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import config #создаем config.py и пишем там: TOKEN = 'TOKEN', скрываем в .gitignore

bot = Bot(token = config.TOKEN)
dp = Dispatcher(bot)
