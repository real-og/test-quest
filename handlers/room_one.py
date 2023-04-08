from aiogram import types
from aiogram.dispatcher import FSMContext
from states import State
import texts
from loader import dp, bot
import keyboards as kb


@dp.message_handler(state=State.first_room_dark)
async def watch_around(message: types.Message):
    if message.text == texts.look_around:
        await message.answer(texts.around_first_room, reply_markup=kb.actions_first_room)
        await State.first_room_looked.set()

@dp.message_handler(state=State.first_room_looked)
async def watch_around(message: types.Message):
    if message.text == texts.go_first_door:
        with open('images/purple.jpeg', 'rb') as img:
            await message.answer_photo(photo=img,
                                       caption=texts.seeing_first_door,
                                       reply_markup=kb.color_glass
                                       )
        await State.first_door.set()
    elif message.text == texts.go_second_door:
        await message.answer(texts.around_first_room, reply_markup=kb.actions_first_room)
        await State.second_door.set()

