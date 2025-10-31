#################################################################
# FILE : board.py
# WRITER : yael bar haim , yaelbarhaim , 315232132
# PROJECT : intro2cs final_project 2024
# DESCRIPTION: Board class for "Chinese Checkers"
#################################################################

import helper
from local_player import LocalPlayer
from computer_player import ComputerPlayer
from marble import Marble
from helper import *
from typing import List, Union
from colorama import Fore


class Board:
    """
    Represents a board object.
    Attributes:
        visual_board (list): A 2D list representing the visual display of the board.
        game_board (dict): A dictionary representing the game state of the board.
    Methods include constructor, add_marble, move_marble etc.
    """

    def __init__(self) -> None:
        """
        A constructor for a Board object.
        :return: None
        """
        self.visual_board = helper.create_board_list()
        self.game_board = helper.create_board_dict(self.visual_board)

    def __str__(self) -> str:
        """
        This function is called when a board object is to be printed,
        and it's creating a string representation of the board.
        :return: str, representing the current status of the board
        """
        board_str = ""
        i = 0
        for row in range(len(self.visual_board)):
            for col in range(len(self.visual_board[0])):
                if self.visual_board[row][col] == 0:
                    board_str += Fore.RESET + " "
                elif self.visual_board[row][col] == 1:
                    board_str += Fore.RESET + "O"
                else:
                    color = helper.string_to_color(self.visual_board[row][col])
                    number = str(self.game_board[(row, col)].get_number())
                    str_to_add = color + number
                    board_str += str_to_add
            if row < len(self.visual_board) - 1:
                board_str += "\n"
            i += 1
        return board_str

    def is_coord_empty(self, coord: Coordinates) -> bool:
        """
        Checks if the provided coord is empty.
        :param coord: Coordinates to check
        :return: True if coord is empty, False otherwise
        """
        return bool(self.game_board[coord] == 0)

    def is_coord_on_board(self, coord: Coordinates) -> bool:
        """
        Checks if the provided coord is on the board.
        :param coord: coordinates to check
        :return: True if coord is on the board, False otherwise
        """
        return coord in self.game_board

    def add_marble(self, marble: Marble) -> bool:
        """
        Adds a marble to the board at the given location.
        :param marble: marble to add
        :return: True if added successfully, False otherwise
        """
        location = marble.get_location()
        if self.is_coord_on_board(location) and self.is_coord_empty(location):  # checks if empty and on board
            x, y = location
            self.game_board[location] = marble
            self.visual_board[x][y] = marble.get_color()[0]
            return True
        else:
            return False

    def step_move_marble(self, marble: Marble, direction: str) -> bool:
        """
        Step-move marble on the board at the given direction.
        Only when the step is valid: the required spot is on board and its empty
        :param marble: marble to move
        :param direction: string, direction to move the marble to. one of VALID_DIRECTIONS
        :return: True if moved successfully, False otherwise
        """
        required = marble.step_requirements(direction)
        if self.is_coord_on_board(required) and self.is_coord_empty(required):   # checks if empty and on board
            new_row, new_col = required
            cur_row, cur_col = marble.get_location()
            self.game_board[required] = marble
            self.visual_board[new_row][new_col] = marble.get_color()[0]
            self.game_board[marble.get_location()] = 0
            self.visual_board[cur_row][cur_col] = 1
            marble.set_location(required)   # update marble's location variable
            return True
        else:
            return False

    def hop_move_marble(self, marble: Marble, direction: str) -> bool:
        """
        Hop-move marble on the board at the given direction.
        Only when the hopping is valid: there's a marble to hop over and an empty on-board spot to hop towards
        :param marble: marble that hop
        :param direction: string, direction to hop the marble to. one of VALID_DIRECTIONS
        :return: True if hopped successfully, False otherwise
        """
        hopped_over = marble.step_requirements(direction)
        hopped_to = marble.hop_requirements(direction)
        if self.is_coord_on_board(hopped_over) and self.is_coord_on_board(hopped_to):  # checks if both on board
            if not self.is_coord_empty(hopped_over) and self.is_coord_empty(hopped_to):
                new_row, new_col = hopped_to
                cur_row, cur_col = marble.get_location()
                self.game_board[hopped_to] = marble
                self.visual_board[new_row][new_col] = marble.get_color()[0]
                self.game_board[marble.get_location()] = 0
                self.visual_board[cur_row][cur_col] = 1
                marble.set_location(hopped_to)  # update marble's location
                return True
            else:
                return False
        else:
            return False

    def marble_possible_steps(self, marble: Marble) -> List[str]:
        """
        List all the possible directions for a given marble to step to.
        :param marble: marble that steps
        :return: list of directions
        """
        possible_steps = []
        for direction in VALID_DIRECTIONS:
            required = marble.step_requirements(direction)
            if self.is_coord_on_board(required) and self.is_coord_empty(required):
                possible_steps.append(direction)
        return possible_steps

    def marble_possible_hops(self, marble: Marble) -> List[str]:
        """
        List all the possible directions for a given marble to hop to.
        :param marble: the marble that hops
        :return: list of directions
        """
        possible_hops = []
        for direction in VALID_DIRECTIONS:
            hoped_over_coord = marble.step_requirements(direction)
            if self.is_coord_on_board(hoped_over_coord) and not self.is_coord_empty(hoped_over_coord):
                hoped_over_marble = self.game_board[hoped_over_coord]
                hoped_to_coord = hoped_over_marble.step_requirements(direction)
                if self.is_coord_on_board(hoped_to_coord) and self.is_coord_empty(hoped_to_coord):
                    possible_hops.append(direction)
        return possible_hops

    def can_marble_step(self, marble: Marble) -> bool:
        """
        Checks if a marble has at least one possible step.
        :param marble: marble to check
        :return: True if the marble has at least one possible step, False otherwise
        """
        return bool(self.marble_possible_steps(marble))

    def can_marble_hop(self, marble: Marble) -> bool:
        """
        Checks if a marble has at least one possible hop.
        :param marble: marble to check
        :return: True if the marble has at least one possible hop, False otherwise
        """
        return bool(self.marble_possible_hops(marble))

    def can_marble_move(self, marble: Marble) -> bool:
        """
        Checks if a given marble has at least one possible move (step or hop).
        :param marble: marble to check
        :return: True if the marble has at least one possible move, False otherwise
        """
        if not self.can_marble_hop(marble) and not self.can_marble_step(marble):
            return False
        else:
            return True

    def list_player_marbles(self, player: Union[LocalPlayer, ComputerPlayer]) -> List[Coordinates]:
        """
        Creates a list of all the player's marbles' coordinates
        :param player:  player whose marbles are being listed
        :return: a list of all player's marbles' coordinates
        """
        players_marbles = []
        for coord in self.game_board:  # checks every coord on board
            if not self.is_coord_empty(coord):
                cur_marble = self.game_board[coord]
                if cur_marble.get_color() == player.get_color():  # checks if it's the player's color
                    players_marbles.append(coord)
        return players_marbles

    def is_player_stuck(self, player: Union[LocalPlayer, ComputerPlayer]) -> bool:
        """
        Checks if at least one of the player's marbles is movable.
        :param player: player whose marbles are being checked
        :return: False if there's at least one marble the player can move, True otherwise
        """
        player_marbles = self.list_player_marbles(player)
        for marble_coord in player_marbles:
            if self.can_marble_move(self.game_board[marble_coord]):
                return False
        return True

    def get_corner_coords(self, corner_num: int) -> List[Coordinates]:
        """
        :param corner_num: corner numer to list all coordinates of
        :return: list of all the coordinates that are in this corner
        """
        if corner_num == 1:
            return CORNER_1
        elif corner_num == 2:
            return CORNER_2
        elif corner_num == 3:
            return CORNER_3
        elif corner_num == 4:
            return CORNER_4
        elif corner_num == 5:
            return CORNER_5
        else:  # corner_num == 6
            return CORNER_6

    def get_target_corner(self, player: Union[LocalPlayer, ComputerPlayer]) -> int:
        """
        Check what corner number is the opposite of the starting corner on the board
        :return: int, target corner number
        """
        player_starting_corner = player.get_corner_num()
        if player_starting_corner == 1:
            return 4
        elif player_starting_corner == 2:
            return 5
        elif player_starting_corner == 3:
            return 6
        elif player_starting_corner == 4:
            return 1
        elif player_starting_corner == 5:
            return 2
        else:  # player_starting_corner == 6
            return 3

    def check_player_won(self, player: Union[LocalPlayer, ComputerPlayer]) -> bool:
        """
        Checks if a given player has won - all the player's marbles are in the opposite corner from where they started.
        :param player: player who is checked
        :return: True if player has won, False otherwise
        """
        player_marbles = self.list_player_marbles(player)
        opposite_corner_num = self.get_target_corner(player)
        opposite_corner = self.get_corner_coords(opposite_corner_num)
        for marble_coord in player_marbles:
            if marble_coord not in opposite_corner:
                return False
        return True

    def convert_to_coords(self, player: LocalPlayer, marble_num: int) -> Coordinates:
        """
        This function converts the marble number of a given player to its coordinates
        :param player: player who's marble number is to be converted
        :param marble_num: marble number to convert
        :return: Coordinates of the marble
        """
        for marble_coords in self.list_player_marbles(player):
            cur_marble = self.game_board[marble_coords]
            if cur_marble.get_number() == marble_num:
                return marble_coords
        return self.list_player_marbles(player)[-1]

