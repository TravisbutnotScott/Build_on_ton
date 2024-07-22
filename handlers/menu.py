# handlers.py
from aiogram import Dispatcher, types
from helper_init import dp, bot
from datetime import datetime, timedelta
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils import executor

FLASK_API_URL = 'http://127.0.0.1:5000'



# Define the menu handler
async def menu(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=2)
    
    # Define the buttons
    buttons = [
        InlineKeyboardButton(text="🏠 How to play?", callback_data="how_to_play"),
        InlineKeyboardButton(text="👥 Invite a Friend", callback_data="invite_friend"),
        InlineKeyboardButton(text="🏆 Leaderboard", callback_data="leaderboard"),
        InlineKeyboardButton(text="✖️ X / TWITTER", url="https://twitter.com/"),
        InlineKeyboardButton(text="💬 Groud \"Build_on_ton\"", url="https://t.me/build_on_ton")
    ]
    STARTPUNCHING = InlineKeyboardButton(text="👷🏼 Lets build!", web_app=WebAppInfo(url="https://crumplum.github.io/greenGarden"))
    # Add buttons to the keyboard
    keyboard.add(STARTPUNCHING).add(*buttons)
    
    # Send the message with the inline keyboard
    await message.answer("Welcome to Build on ton 🏠", reply_markup=keyboard)
    auth_date = int(datetime.utcnow().timestamp())
    data = {
        'query_id': '1',
        'user': message.chat.id,
        'auth_date': int(auth_date)
    }


    print("Bot Data:")
    print(data)
    



# Callback query handler
async def handle_callback(query: types.CallbackQuery):
    if query.data == "how_to_play":
        await query.message.answer("How to play in developing 🏗")
    elif query.data == "invite_friend":
        await query.message.answer("✉️ Invite a Friend in developing 🏗")
    elif query.data == "leaderboard":
        await query.message.answer("🏆 Leaderboard in developing 🏗")
    await query.answer()  # Acknowledge the callback query


# Register the handlers
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(menu, commands="menu")
    dp.register_callback_query_handler(handle_callback, lambda c: c.data in [
        "start_punching",
        "how_to_play",
        "invite_friend",
        "leaderboard"
    ])



