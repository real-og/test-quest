from aiogram.dispatcher.filters.state import StatesGroup, State


class State(StatesGroup):
    first_room_dark = State()
    first_room_looked = State()
    first_door = State()
    second_door = State()
    receiving_code = State()
    glass_room = State()
    checking_locker = State()
    receiving_number_code = State()
    computer_room = State()
