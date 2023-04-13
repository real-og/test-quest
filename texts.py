greeting = 'You open your eyes. Dark room. Metallic smell. Нeadache.'

help = 'The objective is to leave the strange building\n\n/start - begin new run\n\n@bot_dealla - partnership'

around_first_room = 'Eyes adjusted. There are several pieces of glass of different colors on the floor. Picked them up\nSee two doors'

seeing_first_door = 'A metal door glistening <b>purple</b>. There is a field to insert a code and a lens-mechanism into which no more than 2 glasses can be inserted.'
seeing_second_door = 'Metal door with digital panel'

glass_room = 'Beautiful room. The walls are made of thick glass. There is a forest outside. There are no doors. Obviously deadend.'

wrong_code = 'Wrong password'
seeing_locker = 'You see 5 lockers'

def generate_note(first_num):
    note_to_random_code = f"""<b>None</b>

<code>Code : {first_num}......</code>

Then unreadable. looks like 5 numbers in the code, and the first one is - {first_num}

<code>...in case of loss of the code, you may find it out by the selection method. Clicking on the correct number, it activates. If you do not guess, the entire code is reset, but it is not generated again. The numbers are not repeated</code>"""
    return note_to_random_code


garbage_found = 'Some garbage...'

computer_room = 'A room. Old computer is in the middle.\n\n<i>something like Mr Robot</i>'

seeing_game = 'A game pops up.'

alarm_warning = 'The electricity is gone! The evacuation siren starts beeping.\n\n<b>You have 15 seconds to leave the building!</b>\n\n<b>Run!</b>'
alarm_two = 'A beam <b>on top!</b>'
alarm_three = 'The floor is burning <b>from below!</b>'
alarm_four = '<b>Small</b> box!'





look_around = 'Look around'
go_first_door = 'To the first door'
go_second_door = 'To the second door'
enter_code = 'Enter the code'

back = 'Back'
red = '🔴'
yellow = '🟡'
green = '🟢'
blue = '🔵'
black = '⚫️'
colors = [black, yellow, green, blue, red]

check_locker = 'Check the locker'

boxes = ['🗄1️⃣', '🗄2️⃣', '🗄3️⃣', '🗄4️⃣', '🗄5️⃣']

sit_at_comp = 'Sit at the computer'

play = 'Play'


default_ans = "Use the suggested options (keyboard)"

trapped = ""
barrel = "Бочка откатывается в сторону и вы находите тайный туннель.\nВаши действия?"
friend = "Вы начинаете выбираться, но вашему другу не хватает сил.\nОн даёт вам записку.\nВаши действия?"
dark_friend = "Друг даёт вам записку.\nВаши действия?"
note = "В туннеле слишком темно.\nВаши действия?"
light_note = """В записке написано:\n"Не бросай меня здесь."\nВы оставите своего друга или останетесь?"""
beach = "Вы выползаете из туннеля и попадаетет на берег.\nВаши действия?"
boat = "Вы видите на воде судно.\nВаши действия?"
congrats = "Поздавляем, вы отправляетесь в новый мир! Хотите сыграть ещё?"
ending = "Конец.Вы отключаете питание."

reset = '☠️Слишком поздно!☠️\nУдар в спину. Ноги перестают держать. В глазах темнота......'

run = 'Бежать'
duck = 'Нагнуться'
jump = 'Прыгнуть'

stumble = 'Зацепился, потерял 2 секунды'

final_speech = """<b>Вы спаслись!</b>\n\n\n<i>Этот квест - дэмо-проект. Если у вас есть идеи, нужны боты, скрипты, сбор информации, ее анализ, автоматизация процессов либо желание внедрить, где это можно новые технологии, включая ИИ - @bot_dealla</i>"""

leave = 'Уйти'