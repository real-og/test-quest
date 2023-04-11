from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


trapped_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
btn_tr_1 = KeyboardButton('Move the barrel')
btn_tr_2 = KeyboardButton('Sit next to the friend')
trapped_kb.add(btn_tr_1, btn_tr_2)

barrel_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
btn_br_1 = KeyboardButton('Enter the tunnel')
btn_br_2 = KeyboardButton('developing..')
barrel_kb.add(btn_br_1, btn_br_2)

friend_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
btn_fr_1 = KeyboardButton('Read the note')
btn_fr_2 = KeyboardButton('Light a match')
friend_kb.add(btn_fr_1, btn_fr_2)

note_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
btn_nt_1 = KeyboardButton('Leave')
btn_nt_2 = KeyboardButton('developing..')
note_kb.add(btn_nt_1, btn_nt_2)

beach_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
btn_bc_1 = KeyboardButton('Look around')
btn_bc_2 = KeyboardButton('developing..')
beach_kb.add(btn_bc_1, btn_bc_2)

boat_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
btn_bt_1 = KeyboardButton('Board the ship')
btn_bt_2 = KeyboardButton('developing..')
boat_kb.add(btn_bt_1, btn_bt_2)

congrats_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
btn_cg_1 = KeyboardButton('Yes')
btn_cg_2 = KeyboardButton('developing..')
congrats_kb.add(btn_cg_1, btn_cg_2)

light_note_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
btn_ln_1 = KeyboardButton('Stay with the friend')
btn_ln_2 = KeyboardButton('Leave')
light_note_kb.add(btn_ln_1, btn_ln_2)
