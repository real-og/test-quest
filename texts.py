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

trapped = "You and your friend are locked in a dungeon.\nYou see a barrel.\Your actions?"
barrel = "The barrel rolls to the side and you find a secret tunnel.\nYour actions?"
friend = "You start to get out, but your friend does not have enough strength.\nHe gives you a note.\nYour actions?"
dark_friend = "Friend gives you a note.\nYour actions?"
note = "Is it too dark in the tunnel. \nYour actions?"
light_note = """The note says:\n"Don't leave me here."\nWill you leave your friend or will you stay?"""
beach = "You crawl out of the tunnel and get to the shore.\nYour actions?"
boat = "You see a ship on the water.\nYour actions?"
congrats = "Congratulations, you are going to a new world!\nDo you want to play some more?"
ending = "The end. You turn off the power."

reset = '☠️Too late!☠️\nA hit in the back. The legs stop holding. Darkness in the eyes......'

run = 'Run'
duck = 'Duck'
jump = 'Jump'

stumble = 'Stumbled, lost 2 seconds'

final_speech = """<b>You won!</b>\n\n\n<i>This quest is jast a demo. If you have ideas, you need bots, scripts, data collection, analysis, any process automation, using AI - @bot_dealla</i>"""

leave = 'Leave'