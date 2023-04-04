
from aiogram import types
from aiogram.dispatcher import FSMContext

import texts
from loader import dp


@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message):
    await message.answer(texts.greeting)
