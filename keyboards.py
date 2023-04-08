from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from typing import List

import texts

def get_code_keyboard(selected: List[int]):
    kb = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton(text='☑️1️⃣' if 1 in selected else '1️⃣', callback_data='1')
    button_2 = InlineKeyboardButton(text='☑️2️⃣' if 2 in selected else '2️⃣', callback_data='2')
    button_3 = InlineKeyboardButton(text='☑️3️⃣' if 3 in selected else '3️⃣', callback_data='3')
    button_4 = InlineKeyboardButton(text='☑️4️⃣' if 4 in selected else '4️⃣', callback_data='4')
    button_5 = InlineKeyboardButton(text='☑️5️⃣' if 5 in selected else '5️⃣', callback_data='5')
    button_6 = InlineKeyboardButton(text='☑️6️⃣' if 6 in selected else '6️⃣', callback_data='6')
    button_7 = InlineKeyboardButton(text='☑️7️⃣' if 7 in selected else '7️⃣', callback_data='7')
    button_8 = InlineKeyboardButton(text='☑️8️⃣' if 8 in selected else '8️⃣', callback_data='8')
    button_9 = InlineKeyboardButton(text='☑️9️⃣' if 9 in selected else '9️⃣', callback_data='9')
    kb.row(button_1, button_2, button_3)
    kb.row(button_4, button_5, button_6)
    kb.row(button_7, button_8, button_9)
    return kb

look_around = ReplyKeyboardMarkup([[texts.look_around]], resize_keyboard=True)

actions_first_room = ReplyKeyboardMarkup([[texts.go_first_door, texts.go_second_door]], resize_keyboard=True)

colors = [texts.red,
          texts.yellow,
          texts.green,
          texts.blue,
          texts.black]
color_glass = ReplyKeyboardMarkup([colors, [texts.enter_code, texts.back]], resize_keyboard=True)