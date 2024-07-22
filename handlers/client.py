# handlers.py
from aiogram import Dispatcher, types
from helper_init import dp, bot



async def start(message: types.Message):
    await message.reply(f'->DEBUG INF Chat ID: {message.chat.id}<-\nHi-hello🙃, You stared BuildOnTon bot\nGame&chill!😉\nPress /commands for a list of commands', parse_mode='Markdown')
 


async def commands(message: types.Message):
    await message.reply(f'/start\n/socials\n/privacy\n/menu\n', parse_mode='Markdown')


# #Открываем файл files/socials.md в режиме чтения
with open('files/socials.md', 'r') as file:
    content_soc = file.read() # Читаем содержимое файла
#commands=['socials']
async def socials(message: types.Message):
    await message.reply(content_soc, parse_mode='Markdown', disable_web_page_preview=True)

# #Открываем файл files/privacy.md в режиме чтения
with open('files/privacy.md', 'r') as file:
    contentp = file.read() # Читаем содержимое файла
async def privacy(message: types.Message):
    await message.reply(contentp, parse_mode='Markdown', disable_web_page_preview=True)

def register_handlers(dp : Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(commands, commands=['commands','help'])
    dp.register_message_handler(socials, commands=['socials'])
    dp.register_message_handler(privacy, commands=['privacy'])

    