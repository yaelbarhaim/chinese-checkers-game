#################################################################
# FILE : computer_player.py
# WRITER : yael bar haim , yaelbarhaim , 315232132
# PROJECT : intro2cs final_project 2024
# DESCRIPTION: Computer player layer class for "Chinese Checkers"
#################################################################

import random
from helper import *
from typing import List


class ComputerPlayer:
    """
    Represents a computer player object.
    Attributes: name (str), color (str), corner_num (int) = 0, wins (int) = 0, losses (int) = 0
    Methods include: constructor, add_win, add_lose, choose_marble, choose_direction etc.
    """

    def __init__(self, name: str, color: str, corner_num: int = 0, wins: int = 0, losses: int = 0) -> None:
        """
        A constructor for computer player object
        :param name: str, player's name
        :param color: str, player's pawns' color
        :param corner_num: int, players starting corner
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

    def choose_marble(self, player_marbles: List[Coordinates]) -> Coordinates:
        """
        Randomly choose coordinates out of player_marbles list of coordinates
        :param player_marbles: list of coordinates,
        :return: Coordinates
        """
        return random.choice(player_marbles)

    def choose_direction(self) -> str:
        """
        Randomly choose direction from the VALID_DIRECTIONS list
        :return: str, chosen direction
        """
        return random.choice(VALID_DIRECTIONS)

    def hop_choice(self) -> bool:
        """
        Randomly choose Yes or No for hop option
        :return: True or False
        """
        return random.choice([True, False])
