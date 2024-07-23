# основные handlers функции
from aiogram import Dispatcher, types
from helper_init import dp, bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=2)
    
    # Define the buttons
    buttons = [
        InlineKeyboardButton(text="English", callback_data="lang_en"),
        InlineKeyboardButton(text="Русский", callback_data="lang_ru")
    ]

    # Add buttons to the keyboard
    keyboard.add(*buttons)
    
    # Send the message with the inline keyboard
    await message.answer("HELO! Welcome to Build on ton 🏠, \nSelect your preferred language", reply_markup=keyboard)
#message.chat.id, 

# Callback query handler
async def start_callback(query: types.CallbackQuery):
    if query.data == "lang_en":
        await query.message.answer("English")
        lang = 'en'
        




    elif query.data == "lang_ru":
        await query.message.answer("Русский")
        lang = 'ru'








    await query.answer()  # Acknowledge the callback query






#----------------------------------------------------------------------------------------------------------------------------------------------------


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
    #dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(commands, commands=['commands','help'])
    dp.register_message_handler(socials, commands=['socials'])
    dp.register_message_handler(privacy, commands=['privacy'])
    dp.register_message_handler(start, commands="start")
    dp.register_callback_query_handler(start_callback, lambda c: c.data in [
        "lang_en",
        "lang_ru"
    ])


    