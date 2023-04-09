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
    at_computer = State()
    game_start = State()

    trapped_s = State()
    barrel_s = State()
    friend_s = State()
    note_s = State()
    beach_s = State()
    boat_s = State()
    congrats_s = State()
    light_note_s = State()

    alarm_one = State()
    alarm_three = State()
    alarm_two = State()
    alarm_four = State()

    freedom = State()