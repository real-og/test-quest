from aiogram import types
from aiogram.dispatcher import FSMContext
from states import State
import texts
from loader import dp, bot
import keyboards as kb
from codes import GLASSES_CODE
from side_info import file_by_col


@dp.message_handler(state=State.glass_room)
async def watch_around(message: types.Message):
    if message.text == texts.leave:
        await message.answer(texts.around_first_room, reply_markup=kb.actions_first_room)
        await State.first_room_looked.set()