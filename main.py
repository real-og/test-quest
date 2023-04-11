from aiogram import executor
from handlers import *
from loader import dp


if __name__ == '__main__':
    print("Starting test quest bot english")
    executor.start_polling(dp, skip_updates=True)