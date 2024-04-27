# Importing modules and shortcuts from shortcuts.py
from os import system
from time import sleep
from shortcuts import wait, wait_long, clear, new_line

# Create a class that manages players and their respective scores
class Players:

    # Create an empty list of players on object initialization
    def __init__(self):
        self.players = []
        self.repeat = True

    # Add a player to the list of players
    def add_player(self):
        self.current_player = input("Before we start, what is your name? ").lower().strip()
        for player in self.players:
            if player['player'] == self.current_player:
                new_line()
                print("That name has already been used!")
                wait_long()
                return False
        self.players.append({'player': self.current_player, 'correct_questions': 0, 'incorrect_questions': 0})
        for player in self.players:
            if player['player'] == self.current_player:
                self.current_player_stats = player
                break
        new_line()
        print(f"Hi, {self.current_player}, nice to meet you!")
        new_line()
        wait()
        print("We're setting you up now, get ready...")
        new_line()
        wait_long()
        return True

    # Add correct/wrong questions to their data
    def change_player_points(self, score):
        correct_questions = score['correct_answers']
        incorrect_questions = score['incorrect_answers']
        self.current_player_stats['correct_questions'] = correct_questions
        self.current_player_stats['incorrect_questions'] = incorrect_questions

    def current_player_report(self):
        correct_answers = self.current_player_stats['correct_questions']
        incorrect_answers = self.current_player_stats['incorrect_questions']
        total_answers = correct_answers + incorrect_answers
        print(f"You answered {correct_answers} questions correctly and {incorrect_answers} questions incorrectly out of {total_answers}!")
        wait_long()

    def ask_for_repeat(self):
        do_again = input("Do you have any friends who would like to play right now? (yes) ").lower().strip()
        if not (do_again == "" or do_again == "yes"):
            self.repeat = False

    def rearrange(self):
        self.players = sorted(self.players, key=lambda x:x['correct_questions'], reverse=True)

    def all_players_report(self):
        print("Alright, here's a list of everyone's scores:")
        new_line()
        wait()
        for n in range(0, len(self.players)):
            player = self.players[n]
            print(f"{n + 1}. {player['player']} with a score of {player['correct_questions']} out of {player['correct_questions'] + player['incorrect_questions']} questions.")
            wait()