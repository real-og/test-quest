from aiogram import types
from aiogram.dispatcher import FSMContext
from states import State
import texts
from loader import dp, bot
import keyboards as kb
from codes import GLASSES_CODE, PROPER_BOX
from side_info import file_by_col

@dp.message_handler(state=State.second_door)
async def func(message: types.Message, state:FSMContext):
    if message.text == texts.back:
        await message.answer(texts.around_first_room, reply_markup=kb.actions_first_room)
        await State.first_room_looked.set()
    elif message.text == texts.enter_code:
        await message.answer(texts.enter_code, reply_markup=kb.back_kb)
        await State.receiving_number_code.set()
    elif message.text == texts.check_locker:
        await message.answer(texts.seeing_locker, reply_markup=kb.locker_boxes)
        await State.checking_locker.set()

@dp.message_handler(state=State.checking_locker)
async def func(message: types.Message, state:FSMContext):
    if message.text == texts.back:
        await message.answer(texts.seeing_second_door, reply_markup=kb.second_door)
        await State.second_door.set()
    elif message.text in texts.boxes:
        if message.text == PROPER_BOX:
            await message.answer(texts.note_to_random_code, reply_markup=kb.locker_boxes)
        else:
            await message.answer(texts.garbage_found, reply_markup=kb.locker_boxes)



