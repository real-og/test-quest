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
        data = await state.get_data()
        selected = data.get('selected_digits')
        await message.answer(texts.enter_code, reply_markup=kb.get_code_keyboard(selected))
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


@dp.callback_query_handler(state=State.receiving_number_code)
async def send_series(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'back':
        await callback.message.answer(texts.seeing_second_door, reply_markup=kb.second_door)
        await State.second_door.set()
    else:
        tapped_num = int(callback.data)
        data = await state.get_data()
        selected = data.get('selected_digits')
        code = data.get('code')
        position = len(selected)

        if code[position] == tapped_num:
            selected.append(tapped_num)
        else:
            selected = []
        try:
            await bot.edit_message_reply_markup(callback.message.chat.id,
                                callback.message.message_id,
                                reply_markup=kb.get_code_keyboard(selected))
        except:
            pass
        if selected == code:
            selected = []
            await State.computer_room.set()
            await callback.message.answer(texts.computer_room, reply_markup=kb.computer_room)

        await state.update_data(selected_digits=selected) 
    await bot.answer_callback_query(callback.id)