from aiogram import types
from aiogram.dispatcher import FSMContext
from states import State
import texts
from loader import dp, bot
import keyboards as kb
from side_info import file_by_col


@dp.message_handler(state=State.first_room_dark)
async def watch_around(message: types.Message):
    if message.text == texts.look_around:
        await message.answer(texts.around_first_room, reply_markup=kb.actions_first_room)
        await State.first_room_looked.set()

@dp.message_handler(state=State.first_room_looked)
async def handle_action_first_room(message: types.Message, state:FSMContext):
    if message.text == texts.go_first_door:
        data = await state.get_data()
        lenses = data.get('selected_lenses')
        file_img_name = 'images/' + file_by_col[''.join(lenses)]
        with open(file_img_name, 'rb') as file:
            await message.answer_photo(photo=file,
                                       caption=texts.seeing_first_door,
                                       reply_markup=kb.get_glass_kb(lenses)
                                       )
        await State.first_door.set()
    elif message.text == texts.go_second_door:
        await message.answer(texts.seeing_second_door, reply_markup=kb.second_door)
        await State.second_door.set()

