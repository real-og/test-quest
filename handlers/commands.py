
from aiogram import types
from aiogram.dispatcher import FSMContext

import texts
from loader import dp, bot
import keyboards as kb

needed = [7, 4, 3, 9, 1, 2]
selected = []

@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message):
    await message.answer(texts.greeting, reply_markup=kb.get_code_keyboard(selected))

@dp.callback_query_handler()
async def handle_num(callback: types.CallbackQuery):
    print(callback.data)
    selected.append(int(callback.data))
    print('ggggggggggggggggggg')
    if needed == selected:
        await callback.message.answer('Успех')
        selected = []

    # if int(callback.data) is not in needed:
    try:
        await callback.message.edit_reply_markup(reply_markup=kb.get_code_keyboard(selected))
    except:
        pass
    await bot.answer_callback_query(callback.id)
    

