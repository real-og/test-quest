from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from typing import List

import texts

def get_glass_kb(selected):
    colors = [texts.red,
          texts.yellow,
          texts.green,
          texts.blue,
          texts.black]
    for color in selected:
        colors[colors.index(color)] += '✅'
    return ReplyKeyboardMarkup([colors, [texts.enter_code, texts.back]], resize_keyboard=True)

def get_code_keyboard(selected: List[int]):
    kb = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton(text='☑️' if 1 in selected else '1️⃣', callback_data='1')
    button_2 = InlineKeyboardButton(text='☑️' if 2 in selected else '2️⃣', callback_data='2')
    button_3 = InlineKeyboardButton(text='☑️' if 3 in selected else '3️⃣', callback_data='3')
    button_4 = InlineKeyboardButton(text='☑️' if 4 in selected else '4️⃣', callback_data='4')
    button_5 = InlineKeyboardButton(text='☑️' if 5 in selected else '5️⃣', callback_data='5')
    button_6 = InlineKeyboardButton(text='☑️' if 6 in selected else '6️⃣', callback_data='6')
    button_7 = InlineKeyboardButton(text='☑️' if 7 in selected else '7️⃣', callback_data='7')
    button_8 = InlineKeyboardButton(text='☑️' if 8 in selected else '8️⃣', callback_data='8')
    button_9 = InlineKeyboardButton(text='☑️' if 9 in selected else '9️⃣', callback_data='9')
    kb.row(button_1, button_2, button_3)
    kb.row(button_4, button_5, button_6)
    kb.row(button_7, button_8, button_9)
    kb.row(InlineKeyboardButton(text='Назад', callback_data='back'))
    return kb

look_around = ReplyKeyboardMarkup([[texts.look_around]], resize_keyboard=True)

actions_first_room = ReplyKeyboardMarkup([[texts.go_first_door, texts.go_second_door]], resize_keyboard=True)

colors = [texts.red,
          texts.yellow,
          texts.green,
          texts.blue,
          texts.black]
color_glass = ReplyKeyboardMarkup([colors, [texts.enter_code, texts.back]], resize_keyboard=True)

back_kb = ReplyKeyboardMarkup([[texts.back]], resize_keyboard=True)

second_door = ReplyKeyboardMarkup([[texts.enter_code, texts.check_locker], [texts.back]], resize_keyboard=True)

locker_boxes = ReplyKeyboardMarkup([texts.boxes, [texts.back]], resize_keyboard=True)

computer_room = ReplyKeyboardMarkup([[texts.sit_at_comp], [texts.back]], resize_keyboard=True)

at_computer = ReplyKeyboardMarkup([[texts.play], [texts.back]], resize_keyboard=True)

alarm_one = ReplyKeyboardMarkup([[texts.run, texts.duck, texts.jump]], resize_keyboard=True)

glass_room = ReplyKeyboardMarkup([[texts.leave]], resize_keyboard=True)