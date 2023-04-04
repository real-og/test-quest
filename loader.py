from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
import logging
import os


logging.basicConfig(level=logging.WARNING)

API_TOKEN = str(os.environ.get('BOT_TOKEN'))

# storage = RedisStorage2(db=1)
storage = MemoryStorage()
bot = Bot(token=API_TOKEN, parse_mode="HTML")

dp = Dispatcher(bot, storage=storage)