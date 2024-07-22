from helper_init import dp, bot



from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import logging


# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Конфигурация базы данных
DATABASE_URL = "sqlite:///./files/test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Определение модели пользователя
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    tg_id = Column(Integer, unique=True, index=True)
    ref_id = Column(Integer, index=True)
    ref_num = Column(Integer, default=0)
    lang = Column(Text, default='en')


# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

# Настройка бота

WEBHOOK_HOST = 'https://your.domain'
WEBHOOK_PATH = '/webhook/'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

dp.middleware.setup(LoggingMiddleware())

#@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    db: Session = next(get_db())
    user = db.query(User).filter(User.tg_id == message.chat.id).first()
    if not user:
        ref_id = int(message.get_args()) if message.get_args() else None
        new_user = User(tg_id=message.chat.id, ref_id=ref_id)
        db.add(new_user)
        if ref_id:
            referrer = db.query(User).filter(User.tg_id == ref_id).first()
            if referrer:
                referrer.ref_num += 1
        db.commit()
        await message.answer("You have been registered successfully.")
    else:
        await message.answer("You are already registered.")

#@dp.message_handler(commands=['ref'])
async def cmd_ref(message: types.Message):
    ref_link = f"https://t.me/{(await bot.get_me()).username}?start={message.chat.id}"
    await message.answer(f"Here is your referral link: {ref_link}")




# async def start2(message: types.Message):
#     await message.reply(f'/start\n/socials\n/privacy\n/menu\n', parse_mode='Markdown')

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start2")
    dp.register_message_handler(cmd_ref, commands="ref")
    