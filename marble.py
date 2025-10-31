#################################################################
# FILE : marble.py
# WRITER : yael bar haim , yaelbarhaim , 315232132
# PROJECT : intro2cs final_project 2024
# DESCRIPTION: Marble class for "Chinese Checkers"
#################################################################

from typing import Tuple
Coordinates = Tuple[int, int]


class Marble:
    """
    Represents a marble object.
    Attributes: color (str), location (coordinates)
    Methods include: constructor, set_location, movement_requirement etc.
    """

    def __init__(self, color: str, location: Coordinates, number: int) -> None:
        """
        A constructor for a marble object
        :param color: str, the color of the marble
        :param location: coordinates of the marble
        :param number: serves as the name of the marble
        :return: None
        """
        self.__color = color
        self.__location = location
        self.__number = number

    def get_color(self) -> str:
        """
        Returns the color of the marble.
        :return: str, the color of the marble
        """
        return self.__color

    def get_location(self) -> Coordinates:
        """
        Returns the coordinates of the marble.
        :return: Coordinates, the coordinates of the marble
        """
        return self.__location

    def get_number(self) -> int:
        """
        Returns the number of the marble.
        :return: int, the number of the marble
        """
        return self.__number

    def set_location(self, new_location: Coordinates) -> None:
        """
        Sets the location of the marble.
        :param new_location: Coordinates, new coordinates for the marble
        :return: None
        """
        self.__location = new_location

    def step_requirements(self, direction: str) -> Coordinates:
        """
        Determines the required coordinates for the marble to step in a given direction.
        All possible directions are:
        "ul" = up and left
        "ur" = up and right
        "dl" = down and left
        "dr" = down and right
        "jl" = just left = same row and left
        "jr" = just right = same row and right
        :param direction: str, the direction in which to check step requirements
        :return: Coordinates, the required coordinates
        """
        row, col = self.get_location()
        if direction == "jl":
            return row, col - 2
        elif direction == "jr":
            return row, col + 2
        elif direction == "ul":
            return row - 1, col - 1
        elif direction == "ur":
            return row - 1, col + 1
        elif direction == "dl":
            return row + 1, col - 1
        else:   # direction == "dr"
            return row + 1, col + 1

    def hop_requirements(self, direction: str) -> Coordinates:
        """
        Determines the required coordinates for the marble to hop in a given direction.
        All possible directions are:
        "ul" = up and left
        "ur" = up and right
        "dl" = down and left
        "dr" = down and right
        "jl" = just left = same row and left
        "jr" = just right = same row and right
        :param direction: str, the direction in which to check hooping requirements
        :return: Coordinates, the required coordinates
        """
        row, col = self.get_location()
        if direction == "jl":
            return row, col - 4
        elif direction == "jr":
            return row, col + 4
        elif direction == "ul":
            return row - 2, col - 2
        elif direction == "ur":
            return row - 2, col + 2
        elif direction == "dl":
            return row + 2, col - 2
        else:   # direction == "dr"
            return row + 2, col + 2
