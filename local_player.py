#################################################################
# FILE : local_player.py
# WRITER : yael bar haim , yaelbarhaim , 315232132
# PROJECT : intro2cs final_project 2024
# DESCRIPTION: Local player class for "Chinese Checkers"
#################################################################

import helper
from helper import *
from typing import Union
from playsound import playsound


class LocalPlayer:
    """
    Represents a local player object.
    Attributes: name (str), color (str), corner_num (int) = 0, wins (int) = 0, losses (int) = 0
    Methods include: constructor, add_win, add_lose, choose_marble, choose_direction etc.
    """

    def __init__(self, name: str, color: str, corner_num: int = 0, wins: int = 0, losses: int = 0) -> None:
        """
        A constructor for local player object
        :param name: str, player's name
        :param color: str, player's pawns' color
        :param corner_num: int, player's starting corner
        :param wins: int, player's number of wins
        :param losses: int, player's number of losses
        :return: None
        """
        self.__name = name
        self.__color = color
        self.__corner_num = corner_num
        self.__wins = wins
        self.__losses = losses

    def get_name(self) -> str:
        """
        :return: str, player's name
        """
        return self.__name

    def get_color(self) -> str:
        """
        :return: str, player's pawns' color
        """
        return self.__color

    def get_wins(self) -> int:
        """
        :return: int, player's number of wins
        """
        return self.__wins

    def get_losses(self) -> int:
        """
        :return: int, player's number of losses
        """
        return self.__losses

    def get_corner_num(self) -> int:
        """
        :return: int, corner number that player began at
        """
        return self.__corner_num

    def set_wins(self, new_wins: int) -> None:
        """
        Change player's number of wins
        :param new_wins: new number of wins
        :return: None
        """
        self.__wins = new_wins

    def set_losses(self, new_losses: int) -> None:
        """
        Change player's number of losses
        :param new_losses: new number of losses
        :return: None
        """
        self.__losses = new_losses

    def set_corner_num(self, new_corner_num: int) -> None:
        """
        Change player's corner number
        :param new_corner_num: new corner number
        :return: None
        """
        self.__corner_num = new_corner_num

    def add_win(self) -> None:
        """
        Add 1 to player's wins number
        :return: None
        """
        cur_wins = self.get_wins()
        self.set_wins(cur_wins + 1)

    def add_loss(self) -> None:
        """
        Add 1 to player's losses number
        :return: None
        """
        cur_losses = self.get_losses()
        self.set_losses(cur_losses + 1)

    def choose_marble(self) -> Union[int, str]:
        """
        Asks the player to choose a marble (by picking its number).
        (if instead the user enter "logs" then it will pause the game for viewing older games)
        (if instead the user enter "quit" then it will quit the game).
        the function checks if the input is valid - an int and returns the number,
        otherwise it continues the loop until input is valid.
        :return: number of the chosen marble (or "logs" if the user entered it)
        """
        while True:  # runs until user input is valid
            chosen_marble = input("Enter number for marble to move: ")
            if chosen_marble == "logs":     # in case user wants to view old games
                return "logs"
            if chosen_marble == "quit":
                print("ADIOS")
                playsound(helper.get_sound_path("quit"))
                quit()
            try:
                int(chosen_marble)
            except ValueError:
                print("Must enter a number. Please try again")
                playsound(get_sound_path("invalid"))
            else:
                return int(chosen_marble)

    def choose_direction(self) -> str:
        """
        Asks the player to choose direction to move the marble.
        Valid directions are only: "ul", "ur", "dl", "dr", "jl", "jr"
        (up-left, up-right, down-left, down-right, just-left, just-right)
        The function checks if the input is valid.
        If the input was valid it returns the chosen direction,
        otherwise it continues the loop until input is valid.
        :return: string, chosen direction
        """
        while True:  # runs until user input is valid
            chosen_direction = input("Choose a direction to move the marble: ").lower()
            if chosen_direction in VALID_DIRECTIONS:
                return chosen_direction
            else:
                print("Invalid direction. you can only choose from: ul, ur, jl, jr, dl, dr. Please try again.")
                playsound(get_sound_path("invalid"))
                continue
