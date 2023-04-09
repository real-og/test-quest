from aiogram import types
from aiogram.dispatcher import FSMContext
from states import State
import texts
from loader import dp, bot
import keyboards as kb
from codes import GLASSES_CODE, PROPER_BOX
from side_info import file_by_col

@dp.message_handler(state=State.computer_room)
async def func(message: types.Message, state:FSMContext):
    if message.text == texts.back:
        await message.answer(texts.around_first_room, reply_markup=kb.actions_first_room)
        await State.first_room_looked.set()
    elif message.text == texts.sit_at_comp:
        await message.answer(texts.seeing_game, reply_markup=kb.at_computer)
        await State.at_computer.set()

@dp.message_handler(state=State.at_computer)
async def func(message: types.Message, state:FSMContext):
    if message.text == texts.back:
        await message.answer(texts.computer_room, reply_markup=kb.computer_room)
        await State.computer_room.set()
    elif message.text == texts.play:
        await message.answer('начало')
        await State.game_start.set()