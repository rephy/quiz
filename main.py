# Importing classes from other scripts and modules, also imports shortcuts from shortcuts.py
from players import Players
from questions import Questions
from shortcuts import wait, wait_long, clear, new_line

# Initializing the players object
players = Players()

clear()
print("Welcome to Rephy's Trivia Game!")
new_line()
wait()
print("You will be given a variety of questions. You will be able to control the number of questions and the difficulty of them. Your goal is to guess as many as possible. Type A. B, C, D, True, or False.")
new_line()
wait_long()
print("You can have friends play after you, if you want, to see who can get a higher score. For fairness, they'll have to deal with your game settings.")
new_line()
wait_long()
print("We'll give you a summary of you and your friends' score when finished.")
new_line()
wait_long()
clear()

questions = Questions()

questions.new_questions()
clear()

while players.repeat == True:
    if not players.add_player():
        clear()
        continue
    score = questions.ask_questions()
    players.change_player_points(score)
    clear()

    players.current_player_report()
    clear()

    players.ask_for_repeat()
    clear()

players.rearrange()
clear()

players.all_players_report()