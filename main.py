############################################################################################
# FILE : main.py
# WRITER : yael bar haim , yaelbarhaim , 315232132
# PROJECT : intro2cs final_project 2024
# DESCRIPTION: main file to run "Chinese Checkers" game from - regular or capture version
############################################################################################

import helper
from game import Game
from capture import Capture
import pyfiglet  # type: ignore
from rich import print
from helper import *
from playsound import playsound
import sys


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2 and args[1] == "--help":  # prints entire explanation of the program
        helper.print_help()
    elif len(args) == 1:
        title = pyfiglet.figlet_format('Chinese\nCheckers', font='georgia11')
        print(f'[blue]{title}[/blue]')  # title print
        playsound(get_sound_path("new2"))  # intro sound
        if helper.version_choice():
            regular_game = Game()    # creating a new regular game object
            regular_game.run_game()  # starting the game
        else:
            capture_game = Capture()     # creating a new regular game object
            capture_game.play_capture()  # starting the game
