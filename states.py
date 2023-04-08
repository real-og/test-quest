from aiogram.dispatcher.filters.state import StatesGroup, State


class State(StatesGroup):
    start_entry = State()
    first_room_looked = State()
    first_door = State()
    second_door = State()
    receiving_code = State()
    glass_room = State()
