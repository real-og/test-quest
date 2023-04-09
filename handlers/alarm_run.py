from aiogram import types
from aiogram.dispatcher import FSMContext
from states import State
import texts
from loader import dp
import keyboards as kb
import asyncio

@dp.message_handler(state=State.alarm_one)
async def func(message: types.Message, state:FSMContext):
    if message.text == texts.run:
        pass
    elif message.text in (texts.jump, texts.duck):
        await message.answer(texts.stumble)
        await asyncio.sleep(2)
    await message.answer(texts.alarm_two,  reply_markup=kb.alarm_one)
    await State.alarm_two.set()

@dp.message_handler(state=State.alarm_two)
async def func(message: types.Message, state:FSMContext):
    if message.text == texts.duck:
        pass
    elif message.text in (texts.jump, texts.run):
        await message.answer(texts.stumble)
        await asyncio.sleep(2)
    await message.answer(texts.alarm_three,  reply_markup=kb.alarm_one)
    await State.alarm_three.set()

@dp.message_handler(state=State.alarm_three)
async def func(message: types.Message, state:FSMContext):
    if message.text == texts.jump:
        pass
    elif message.text in (texts.duck, texts.run):
        await message.answer(texts.stumble)
        await asyncio.sleep(2)
    await message.answer(texts.alarm_four,  reply_markup=kb.alarm_one)
    await State.alarm_four.set()

@dp.message_handler(state=State.alarm_four)
async def func(message: types.Message, state:FSMContext):
    if message.text == texts.jump:
        await state.update_data(escape=True)
    elif message.text in (texts.duck, texts.run):
        await message.answer(texts.stumble)
        await asyncio.sleep(2)
    await state.update_data(escape=True)
    await message.answer(texts.final_speech)
    await State.freedom.set()