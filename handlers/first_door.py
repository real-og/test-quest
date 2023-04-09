from aiogram import types
from aiogram.dispatcher import FSMContext
from states import State
import texts
from loader import dp, bot
import keyboards as kb
from codes import GLASSES_CODE
from side_info import file_by_col

@dp.message_handler(state=State.first_door)
async def func(message: types.Message, state:FSMContext):
    tapped_color = message.text.replace('✅', '').strip()
    if message.text == texts.back:
        await message.answer(texts.around_first_room, reply_markup=kb.actions_first_room)
        await State.first_room_looked.set()
    elif message.text == texts.enter_code:
        await message.answer(texts.enter_code, reply_markup=kb.back_kb)
        await State.receiving_code.set()

    elif tapped_color in texts.colors:
        data = await state.get_data()
        lenses = data.get('selected_lenses')
        if tapped_color in lenses:
            lenses.remove(tapped_color)
        elif len(lenses) < 2:
            lenses.append(tapped_color)
        file_img_name = 'images/' + file_by_col[''.join(lenses)]
        await state.update_data(selected_lenses=lenses)
        with open(file_img_name, 'rb') as file:
            await message.answer_photo(file, reply_markup=kb.get_glass_kb(lenses))



@dp.message_handler(state=State.receiving_code)
async def func(message: types.Message, state:FSMContext):
    if message.text == GLASSES_CODE:
        await message.answer(texts.glass_room, reply_markup=kb.glass_room)
        await State.glass_room.set()
    elif message.text == texts.back:
        data = await state.get_data()
        lenses = data.get('selected_lenses')
        file_img_name = 'images/' + file_by_col[''.join(lenses)]
        with open(file_img_name, 'rb') as file:
            await message.answer_photo(photo=file,
                                       caption=texts.seeing_first_door,
                                       reply_markup=kb.get_glass_kb(lenses)
                                       )
        await State.first_door.set()
    else:
        await message.answer(texts.wrong_code, reply_markup=kb.back_kb)








