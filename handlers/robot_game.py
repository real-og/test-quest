from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import texts
import os
from keyboards_robot import trapped_kb, barrel_kb, friend_kb, note_kb, beach_kb, boat_kb, congrats_kb, light_note_kb
from aiogram import types
from aiogram.dispatcher import FSMContext
from states import State
import texts
from loader import dp, bot
import keyboards as kb
from codes import GLASSES_CODE, PROPER_BOX
from side_info import file_by_col
from handlers.commands import send_welcome
import asyncio

@dp.message_handler(state=State.trapped_s)
async def get_barrel(message: types.Message):
    input = message.text
    if input == 'Move the barrel':
        await message.answer_photo(photo=types.InputFile('images_robot/barrel.jpg'),
                                    caption=texts.barrel,
                                    reply_markup=barrel_kb)
        await State.barrel_s.set()
    elif input == 'Sit next to the friend':
        await message.answer_photo(photo=types.InputFile('images_robot/darknote.jpg'),
                                    caption=texts.dark_friend,
                                    reply_markup=friend_kb)
        await State.friend_s.set()
    else:
        await message.answer(texts.default_ans, reply_markup=trapped_kb)


@dp.message_handler(state=State.barrel_s)
async def get_friend(message: types.Message):
    input = message.text
    if input == 'Enter the tunnel':
        await message.answer_photo(photo=types.InputFile('images_robot/friend.jpg'),
                                    caption=texts.friend,
                                    reply_markup=friend_kb)
        await State.friend_s.set()
    else:
        await message.answer(texts.default_ans, reply_markup=barrel_kb)


@dp.message_handler(state=State.friend_s)
async def get_note(message: types.Message):
    input = message.text
    if input == 'Read the note':
        await message.answer_photo(photo=types.InputFile('images_robot/note.jpg'),
                                    caption=texts.note,
                                    reply_markup=note_kb)
        await State.note_s.set()
    elif input == 'Light a match':
        await message.answer_photo(photo=types.InputFile('images_robot/dontleave.jpg'),
                                    caption=texts.light_note,
                                    reply_markup=light_note_kb)
        await State.light_note_s.set()
    else:
        await message.answer(texts.default_ans, reply_markup=friend_kb)


async def reset_to_start(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('escape'):
        return
    await message.answer(texts.reset)
    await send_welcome(message, state)

#ending one
@dp.message_handler(state=State.light_note_s)
async def get_congrats(message: types.Message, state: FSMContext):
    input = message.text
    if input == 'Stay with the friend':
        await message.answer_photo(photo=types.InputFile('images_robot/end.png'),
                                    reply_markup=congrats_kb)
        await message.answer(texts.ending, reply_markup=kb.alarm_one)
        await state.update_data(escape=False)
        
        async def call_my_function():
            await asyncio.sleep(10)
            await reset_to_start(message, state)
        asyncio.create_task(call_my_function())

        await message.answer(texts.alarm_warning, reply_markup=kb.alarm_one)
        await State.alarm_one.set()

    elif input == 'Leave':
        await(get_beach(message))
    else:
        await message.answer(texts.default_ans, reply_markup=light_note_kb)


@dp.message_handler(state=State.note_s)
async def get_beach(message: types.Message):
    input = message.text
    if input == 'Leave':
        await message.answer_photo(photo=types.InputFile('images_robot/beach.jpg'),
                                    caption=texts.beach,
                                    reply_markup=beach_kb)
        await State.beach_s.set()
    else:
        await message.answer(texts.default_ans, reply_markup=note_kb)


@dp.message_handler(state=State.beach_s)
async def get_boat(message: types.Message):
    input = message.text
    if input == 'Look around':
        await message.answer_photo(photo=types.InputFile('images_robot/boat.jpg'),
                                    caption=texts.boat,
                                    reply_markup=boat_kb)
        await State.boat_s.set()
    else:
        await message.answer(texts.default_ans, reply_markup=beach_kb)


@dp.message_handler(state=State.boat_s)
async def get_congrats(message: types.Message):
    input = message.text
    if input == 'Board the ship':
        await message.answer_photo(photo=types.InputFile('images_robot/congrats.jpg'),
                                    caption=texts.congrats,
                                    reply_markup=congrats_kb)
        await State.congrats_s.set()
    else:
        await message.answer(texts.default_ans, reply_markup=boat_kb)


@dp.message_handler(state=State.congrats_s)
async def get_menu(message: types.Message):
    if message.text == 'Yes':
        await message.answer_photo(photo=types.InputFile('images_robot/trapped.jpg'),
                            caption=texts.trapped,
                            reply_markup=trapped_kb)
        await State.trapped_s.set()
    else:
        await message.answer(texts.default_ans, reply_markup=congrats_kb)


