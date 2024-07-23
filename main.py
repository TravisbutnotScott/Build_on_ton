# 👉 🙏 👆 🤖 ❤️ 💪 ✍️ 🎯 ✖️ ⛔ ✅ 📊 📈 🧮 🏠 👷🏼 🏗
#import json, time, random
import time

from aiogram.utils import executor
from helper_init import dp, bot

#регестрация handlers
from handlers import client, menu, db_start

client.register_handlers(dp)
menu.register_handlers(dp)
db_start.register_handlers(dp)








 
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    while True:  # запускаем бесконечный цикл
        try:  # пробуем наладить связь с сервером Telegram
            bot.polling(none_stop=True)  # polling отправляет запросы на сервара
        except Exception as e:  # если произойдет ошибка, то
            time.sleep(3)  # подождать 3 секунды
            print(e)  # и вывести logi ошибки в консоль компьютера

#//////////////////////////////////////////////////////////////////////////////////////////    
