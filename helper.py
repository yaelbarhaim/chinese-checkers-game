################################################################################################
# FILE : helper.py
# WRITER : yael bar haim , yaelbarhaim , 315232132
# PROJECT : intro2cs final_project 2024
# DESCRIPTION: Helper file for "Chinese Checkers". contains imports, constants, functions etc.
################################################################################################

from typing import List, Tuple, Any, Union, Dict
from colorama import Fore
import os
from playsound import playsound

##################################################################
# Constants used in the program:
##################################################################

Coordinates = Tuple[int, int]

PLACES_NUM_IN_EACH_ROW = [1, 2, 3, 4, 13, 12, 11, 10, 9, 10, 11, 12, 13, 4, 3, 2, 1]
# represents number of holes in each row of "Chinese Checkers" board

VALID_DIRECTIONS = ["ul", "ur", "dl", "dr", "jl", "jr"]
# stands for: up-left, up-right, down-left, down-right, just-left, just-right

VALID_COLORS = ["R", "B", "G", "P", "C", "Y"]
# stands for: RED, BLUE, GREEN, PINK, CYAN, YELLOW

CORNER_1 = [(0, 12), (1, 11), (1, 13), (2, 10), (2, 12), (2, 14), (3, 9), (3, 11), (3, 13), (3, 15)]
CORNER_2 = [(4, 18), (4, 20), (4, 22), (4, 24), (5, 19), (5, 21), (5, 23), (6, 20), (6, 22), (7, 21)]
CORNER_3 = [(9, 21), (10, 20), (10, 22), (11, 19), (11, 21), (11, 23), (12, 18), (12, 20), (12, 22), (12, 24)]
CORNER_4 = [(13, 9), (13, 11), (13, 13), (13, 15), (14, 10), (14, 12), (14, 14), (15, 11), (15, 13), (16, 12)]
CORNER_5 = [(12, 0), (12, 2), (12, 4), (12, 6), (11, 1), (11, 3), (11, 5), (10, 2), (10, 4), (9, 3)]
CORNER_6 = [(4, 0), (4, 2), (4, 4), (4, 6), (5, 1), (5, 3), (5, 5), (6, 2), (6, 4), (7, 3)]
# those corners lists represent all the coordinates in each corner of the board of our game.
# it is numbered when the top corner is number 1 and the count is clockwise.


##################################################################
# Functions used in the program:
##################################################################

###################
# Used in board.py:
###################

def create_board_list() -> List[List[Any]]:
    """
    This function creates a list representing the board of "Chinese Checkers".
    It contains 17 rows and 25 columns. this is because the number 25 allows us to place
    The holes in just even or just uneven places which makes it more accurate.
    1 represent a hole and 0 represent an out-of-border place which is there to even the placement.
    :return: a list representing the board
    """
    board_list = []
    for places in PLACES_NUM_IN_EACH_ROW:  # ech row has a different amount of holes
        new_row = []
        each_side = int((25 - (2 * places - 1)) / 2)  # calculating spaces until and after the holes
        for left_side in range(each_side):  # adding all the left side of the row
            new_row.append(0)
        for num in range(places):  # adding all the holes for the marbles with separation
            new_row.append(1)
            if num < places - 1:
                new_row.append(0)
        for right_side in range(each_side):  # adding all the right side of the row
            new_row.append(0)
        board_list.append(new_row)
    return board_list


def create_board_dict(board_list: List[List[int]]) -> Dict[Tuple[int, int], Any]:
    """
    This function creates a dictionary representing the board based on the provided 2D list of the board.
    contains only the hole's (valid places) coordinates as keys and set their values to 0 that represent it's empty.
    :param board_list: a 2D list of the board. 1 represents the holes and 0 represents out of border place.
    :return: dictionary that maps each coord on board to what's in it (empty or marble)
    """
    board_dict = {}
    for i in range(len(board_list)):
        for j in range(len(board_list[0])):
            if board_list[i][j] == 1:
                board_dict[(i, j)] = 0
    return board_dict


def string_to_color(string: str) -> str:
    """
    This function converts a string to a Fore color using colorama lib
    :param string: str representing the color - first letter in capital case of it
    :return: str, the color
    """
    if string == "B":
        return Fore.BLUE
    elif string == "C":
        return Fore.CYAN
    elif string == "G":
        return Fore.GREEN
    elif string == "P":
        return Fore.MAGENTA
    elif string == "R":
        return Fore.RED
    else:
        return Fore.YELLOW


#################
# Used in log.py
#################

def logs_folder() -> None:
    """
    If it doesn't exist, this function creates a new folder for all logs files.
    :return: None
    """
    folder_name = "logs"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def naming_game() -> str:
    """
    Creates a new name for the game by searching for the next non-taken number in the games' names in the folder "logs"
    :return: string, new name for the game
    """
    i = 1
    while True:
        file_name = f"game_{i}.txt"
        file_path = os.path.join(os.getcwd(), "logs", file_name)
        if not os.path.exists(file_path):
            return file_name
        else:
            i += 1


##################
# Used in game.py:
##################

def load_older_option() -> bool:
    """
    Asks the user if they want to start a new game or view an older one
    :return: True if user want to resume to an older game, False otherwise
    """
    while True:
        option = input("Start a new game / Load an older game ? (new/old) ")
        if option.lower() == "new":
            return False
        elif option.lower() == "old":
            return True
        else:
            print("Invalid input. Please enter 'new' or 'old'.")
            continue


def choose_game() -> Tuple[str, str]:
    """
    Asks the user to choose the number of the game they want to load and see.
    If the player enter: "quit" then the program will exit the game.
    :return: tuple of strings, path to the chosen game and the name of the game.
    """
    while True:
        answer = input("Enter number of game to resume: ")
        if answer == "quit":
            quit(print("ADIOS"))
        path = os.path.join(os.getcwd(), "logs", "game_" + answer + ".txt")
        if not os.path.exists(path):
            print("There no such game. Please try again")
            playsound(get_sound_path("invalid"))
        elif did_game_over(path):
            read_any_log(path)
            print("This game has already ended so you view it but not resume it. Please try again")
        else:
            game_name = "game_" + answer + ".txt"
            return path, game_name


def choose_game_to_read() -> Tuple[str, str]:
    """
    Asks the user to choose the number of the game they want to view.
    If the player enter: "quit" then the program will exit the game.
    :return: tuple of strings, path to the chosen game and the name of the game.
    """
    while True:
        answer = input("Enter number of game to view: ")
        if answer == "quit":
            quit(print("ADIOS"))
        path = os.path.join(os.getcwd(), "logs", "game_" + answer + ".txt")
        if not os.path.exists(path):
            print("There no such game. Please try again")
            playsound(get_sound_path("invalid"))
        else:
            game_name = "game_" + answer + ".txt"
            return path, game_name


def did_game_over(game_path: str) -> bool:
    """
    Checks if the game ended
    :param game_path: path to the log file of the game
    :return: True if the game ended, False otherwise
    """
    with open(game_path, "r") as file:
        content = file.read()
        if "WINNER:" in content:
            return True
        else:
            return False


def resume_option() -> bool:
    """
    Asks the user if they want to resume the game or start a new one
    :return: True if user want to play this game, False otherwise
    """
    while True:
        option = input("Do you want to continue this game? (y/n) ")
        if option.lower() == "y":
            print("BACK TO BUSINESS:")
            return True
        elif option.lower() == "n":
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'")
            playsound(get_sound_path("invalid"))
            continue


def collect_players_info(game_path: str) -> List[List[str]]:
    """
    Collect from log file all the players' info and arrange them in the list of lists.
    Each inner list contains a different player's info in this form: [name, color, corner, wins, losses, type]
    :param game_path: path to log file of the game
    :return: 2D list of players' info
    """
    players_info = []
    with open(game_path, "r") as log_file:
        line_num = 0
        for line in log_file.readlines():
            if "Name: " in line:           # meaning it's a player in the game
                new_player = []
                clean_line = line[:-1]     # removes the "\n" sign
                attributes = clean_line.split(", ")     # splits into player's attributes
                for attribute in attributes:
                    new_player.append(attribute.split(": ")[1])
                players_info.append(new_player)
            elif line_num > 8:
                break
            line_num += 1
        return players_info


def is_there_board(game_path: str) -> bool:
    """
    Checks if a board was already created for the game
    :param game_path: path to the log file of the game
    :return: True if there is a board already, False otherwise
        """
    with open(game_path, "r") as log_file:
        for line in log_file.readlines():
            if "State of the board:" in line:
                return True
            else:
                continue
        return False


def marbles_info_helper_1(game_path: str) -> str:
    """
    This function return a sub-string out of a log file. Specifically the last marbles state in the file
    :param game_path: path to the log file of the game
    :return: string of the last marbles state
    """
    marbles_str = ""
    with open(game_path, "r") as log_file:
        lines = log_file.readlines()
        length = len(lines)
        i = 0
        for line in lines[::-1]:
            if "Marbles state: " in line:
                start_index = i
                break
            else:
                i += 1
        for line in lines[length-i:]:
            marbles_str += line
    return marbles_str


def marbles_info_helper_2(marbles_str: str) -> List[List[str]]:
    """
    This function gets a str and transform it to a list of lists, so it will be cleaner.
    It lists all marbles information but still in strings.
    :param marbles_str: string of the last marbles state
    :return: list of lists with marbles information
    """
    clean_marbles_list = []
    str_split = marbles_str.split("], ")
    for cur_marble in str_split:
        if "\n" in cur_marble:
            continue
        else:
            new_marble = []
            cur_marble = cur_marble.strip("[]")
            split_marble = cur_marble.split(" : ")
            for char in split_marble:
                new_marble.append(char)
            clean_marbles_list.append(new_marble)
    return clean_marbles_list


def marbles_info_helper_3(string_list: List[List[str]]) -> List[List[Union[str, Coordinates, int]]]:
    """
    This function gets a list of strings with the marbles info and returns a list of it but now with integers
    And coordinates where needed.
    :param string_list: list of strings with marbles info
    :return: list of lists with marbles information
    """
    fixed_list = []
    for marble in string_list:
        new_marble: List[Union[str, Coordinates, int]] = []
        color = marble[0]
        first_loc = marble[1].strip("()")
        loc = first_loc.split(",")
        row, col = int(loc[0]), int(loc[1])
        num = int(marble[2])
        new_marble.append(color)
        new_marble.append((row, col))
        new_marble.append(num)
        fixed_list.append(new_marble)
    return fixed_list


def collect_marbles_info(game_path: str) -> List[List[Union[str, Coordinates, int]]]:
    """
    This function gets a path to log file and returns a list with all the marbles' info of the last  state.
    Each inner list is of a marble on board and in the form of [color, coordinates, number]
    :param game_path: path to log file
    :return: list of lists when each inner list contains attributes of a marble on board
    """
    marble_str = marbles_info_helper_1(game_path)
    cleaner_list = marbles_info_helper_2(marble_str)
    final_list = marbles_info_helper_3(cleaner_list)
    return final_list


def last_played(game_path: str) -> str:
    """
    This function gets a path to log file and returns a str of the last played player's name.
    :param game_path: path to log file
    :return: str of last player
    """
    with open(game_path) as log_file:
        for line in log_file.readlines():
            if "PLAYER: " in line:
                cur_player = line[8:-6]
        return cur_player


def read_any_log(game_path: str) -> None:
    """
    This function gets a path to log file and prints its content
    :param game_path: path to log file
    :return: None
    """
    with open(game_path, "r") as file:
        content = file.read()
        print(content)
        print("################### END OF GAME LOG ###################" + "\n")


def choose_players_num() -> int:
    """
    Asks the user to choose the total number of players for the game (including computer player)
    :return: int, number of players
    """
    while True:
        number_of_players = input(Fore.RESET + "How many players are playing? (including computer players) ")
        if number_of_players == "2":
            return 2
        elif number_of_players == "3":
            return 3
        elif number_of_players == "4":
            return 4
        elif number_of_players == "6":
            return 6
        else:
            print("Number of players can only be: 2, 3, 4 or 6")
            playsound(get_sound_path("invalid"))
            continue


def choose_local_num(total_players_number: int) -> int:
    """
    Asks the user to choose the number of local players for the game (not including the computer players)
    :param total_players_number: int, number of players including the computer players
    :return: int, number of local players
    """
    while True:
        answer = input("How many local players are playing? (the rest will be computer players) ")
        try:
            locals_num = int(answer)
        except ValueError:
            print("Invalid number, please try again")
            playsound(get_sound_path("invalid"))
            continue
        else:
            if locals_num > total_players_number or locals_num < 1:
                print("Invalid number, please try again")
                playsound(get_sound_path("invalid"))
                continue
            else:
                return locals_num


def get_sound_path(selected_sound: str) -> str:
    """
    This function gets a string of a specific sound and returns the path of the file to be played
    :param selected_sound: str, name of the sound to play
    :return: str, path of the file to be played
    """
    return os.path.join(os.getcwd(), "sounds", selected_sound+".mp3")


##################
# Used in main.py:
##################

def version_choice() -> bool:
    """
    Asks the user to select a version of the game to play.
    :return: True if they want regular, False if they want capture
    """
    while True:
        version = input("Do you want to play the REGULAR version or the CAPTURE version? (r/c) ")
        if version.lower() == "r":
            return True
        elif version.lower() == "c":
            return False
        else:
            print("Answer must be either r or c, please try again.")
            playsound(get_sound_path("invalid"))
            continue


def print_help() -> None:
    """
    This function prints the help message with the entire explanation of the program.
    :return: None
    """
    info = "\nCHINESE CHECKERS GAME EXPLANATION\n\n"
    info += "To begin with, you will be asked to choose a version to play - Regular or Capture (answer: r/c).\n\n"
    info += "REGULAR GAME:\n"
    info += "A regular game split into 2 options:\n   1. Start a new game\n   2. Load an older game\n"
    info += ("OLDER GAME OPTION: \nPlayer chooses a number of an older game they want to view.\nIf the game exist, it"
             " will show up, and then the player can choose if they want to resume where it stopped.\n"
             "Answer will be y/n. y - will resume the game, n - will get back to main menu.\n")
    info += ("NEW GAME OPTION: \n1. User chooses total number of players (including computer ones) and then "
             "what number out of them are local players.\n   Total number can be 2, 3, 4, or 6. Local players number "
             "can be 1-6 accordingly.\n")
    info += ("2. Each local player will pick a name and a color.\n"
             "   Name needs to be no longer than 25 characters and not include the sings: , or : .\n"
             "   Color can be any one of the following: R (red), G (green), B (blue), Y (yellow), C (cyan), P (pink).\n"
             "   Both must be non-taken.\n")
    info += ("RULES OF THE GAME:\nThe goal is to move all of your marbles into the opposite corner"
             " from where you started. First player to do so - wins the game.\n"
             "Moves are either a step to an empty adjacent spot, or a hop over an adjacent"
             " marble straight into an empty spot. A hop also allows multiple hops in a row if possible.\n")
    info += "THE COURSE OF THE GAME:\n"
    info += ("1. Picking a marble to move - player will choose a number between 0-9 and the chosen marble is the one "
             "that is represented by that number in the player's color.\n"
             "   If the marble is unmovable, the player will choose again. In case all the player's marble are "
             "unmovable, the player's turn is skipped.\n")
    info += ("   At any point of choosing the marble, there are two more options for the user:\n"
             "      A. Entering 'quit' to quit the game.\n"
             "      B. Entering 'logs' to view older games (to learn strategy"
             " for example).\n"
             "      Player can return to the current game (not the viewed one) after watching the game "
             "they wanted.\n")
    info += ("2. Move type choice - if the marble can both step and hop then the player "
             "will choose what move they would like to commit (step/hop).\n"
             "   Else, this stage is ignored and the type of move that is possible is automatically chosen.\n")
    info += ("3. Picking direction to move the marble to - player will enter direction for the chosen movement.\n"
             "   Valid directions are: ur (up-right), ul (up-left), dr (down-right), dl (down-left), jr (just-right), "
             "jl (just-left).\n") + "   The correct format is entering both letters without anything else.\n"
    info += ("4. After the game is over, all players' wins and losses numbers are updated according to the score, "
             "and another game with the same players is offered to the user.\n\n")
    info += ("CAPTURE GAME:\n1. User choose total number of players (including computer ones) and then "
             "what number out of them are local players.\n   Total number can be 2-6. Local players number "
             "can be 1-6 accordingly.\n")
    info += ("2. Each local player will pick a name.\n"
             "   Name needs to be non-taken, no longer than 25 characters and not include the sings: , or : .\n")
    info += ("RULES OF THE GAME:\nYou can pick any marble on board and the only move that's allowed is"
             " hop (Multiple hops in a row are allowed if possible).\nEach hopped over marble gets 'eaten' "
             "by the player and adds them a point."
             "The goal is to gain as many points as possible.\nThe game ends when there are no more hops available, "
             "and the winner is the player with the highest score.\n")
    info += "THE COURSE OF THE GAME:\n"
    info += ("1. Picking a marble to move - player will enter the first letter of the color of the marble, "
             "followed by its number.\n   The correct format is both of those characters without anything else."
             " For example: B6 (blue 6).\n"
             "   If the marble can not hop, the player will choose again.\n")
    info += "   At any point of choosing the marble, entering 'quit' will quit the game.\n"
    info += ("2. Picking direction to move the marble to - player will enter direction for hopping.\n"
             "   Valid directions are: ur (up-right), ul (up-left), dr (down-right), dl (down-left), jr (just-right), "
             "jl (just-left).\n") + "   The correct format is entering both letters without anything else.\n"
    info += ("3. After the game is over, all players' wins and losses numbers are updated according to the score, "
             "and another game with the same players is offered to the user.\n")
    print(info)
