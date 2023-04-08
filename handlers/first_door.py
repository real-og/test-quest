from aiogram import types
from aiogram.dispatcher import FSMContext
from states import State
import texts
from loader import dp, bot
import keyboards as kb
from codes import GLASSES_CODE

@dp.message_handler(state=State.first_door)
async def func(message: types.Message):
    if message.text == texts.back:
        await message.answer(texts.around_first_room, reply_markup=kb.actions_first_room)
        await State.first_room_looked.set()
    elif message.text == texts.enter_code:
        await message.answer(texts.enter_code)
        await State.receiving_code.set()
    else:
        await message.answer(message.text)

@dp.message_handler(state=State.receiving_code)
async def func(message: types.Message):
    if message.text == GLASSES_CODE:
        await message.answer(texts.glass_room)
        await State.glass_room.set()
    elif message.text == texts.back:
        with open('images/purple.jpeg', 'rb') as img:
            await message.answer_photo(photo=img,
                                       caption=texts.seeing_first_door,
                                       reply_markup=kb.color_glass
                                       )
        await State.first_door.set()
    else:
        await message.answer(texts.wrong_code)








