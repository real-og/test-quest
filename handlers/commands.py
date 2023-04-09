
from aiogram import types
from aiogram.dispatcher import FSMContext
from states import State
# from aiogram.dispatcher.filters.state import State
import texts
from loader import dp, bot
import keyboards as kb
import random
import asyncio

@dp.message_handler(commands=['help'], state="*")
async def send_help(message: types.Message):
    await message.answer(texts.help)


@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    target_code = random.sample(range(1, 10), 5)
    await state.update_data(selected_lenses=[],
                            selected_digits=[],
                            code=target_code,
                            escape=True
                            )
    print(target_code)
    await message.answer(texts.greeting, reply_markup=kb.look_around)
    await State.first_room_dark.set()



