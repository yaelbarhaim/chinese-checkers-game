#################################################################
# FILE : game.py
# WRITER : yael bar haim , yaelbarhaim , 315232132
# PROJECT : intro2cs final_project 2024
# DESCRIPTION: Game class for "Chinese Checkers"
#################################################################

import helper
from board import Board
from local_player import LocalPlayer
from computer_player import ComputerPlayer
from marble import Marble
from log import Log
import random
import datetime
from helper import *
from playsound import playsound
from typing import List, Union, Any, Tuple


class Game:
    """
    Represents a game object - responsible for managing the flow of the game and its rules.
    Attributes: board (Board), players_number (int), local_players_number (int), players_list (List[Player]),
    log (Log).
    Methods include:
        1. General settings methods
        2. New game settings methods
        3. older game resume settings methods
        4. Log file managing methods
        5. Game run managing methods
    """

    def __init__(self) -> None:
        """
        A constructor for Game object
        """
        self.board = Board()
        self.__players_num = 0  # total amount of players in this game
        self.__local_players_num = 0  # number of local players out of the total
        self.__players_list: List[Union[LocalPlayer, ComputerPlayer]] = []
        self.__log = Log()

    ####################################################################################
    # SETTINGS
    # all methods below are settings related - before the start of the game
    ####################################################################################

    def get_players_num(self) -> int:
        """
        Returns the total number of players in the game.
        :return: int, number of players
        """
        return self.__players_num

    def set_players_num(self, players_num: int) -> None:
        """
        Changes the number of players in the game to a given new number.
        :param players_num: new number of players
        :return: None
        """
        self.__players_num = players_num

    def get_local_players_num(self) -> int:
        """
        Returns the number of local players in the game.
        :return: int, number of local players
        """
        return self.__local_players_num

    def set_local_players_num(self, local_players_num: int) -> None:
        """
        Changes the number of local players in the game to a given new number.
        :param local_players_num: new number of local players
        :return: None
        """
        self.__local_players_num = local_players_num

    def get_players_list(self) -> list[Union[LocalPlayer, ComputerPlayer]]:
        """
        Returns the list of all the players in the game.
        :return: list of player objects in the game
        """
        return self.__players_list

    def get_log(self) -> Log:
        """
        Returns the log object of the game.
        :return: Log
        """
        return self.__log

    def set_log(self) -> None:
        """
        Changes the log object of the game by creating a new log object for it.
        :return: None
        """
        self.__log = Log()

    def add_player(self, player: Union[LocalPlayer, ComputerPlayer]) -> None:
        """
        Adds a player to the players list
        :param player: Player object to add
        :return: None
        """
        cur_listed = self.get_players_list()
        cur_listed.append(player)

    ####################################################################################
    # NEW GAME SETTINGS
    # all methods below are for settings of a new game
    ####################################################################################

    def set_coords_to_player(self, coords_list: List[Coordinates], player: Union[LocalPlayer, ComputerPlayer]) -> None:
        """
        Adding a given player's marbles to all the coords in a given list. used for the set-up of the game
        :param coords_list: list of coordinates, to which the player's marbles will be added
        :param player: local player or computer player
        :return: None
        """
        players_color = player.get_color()
        i = 0
        for coord in coords_list:
            cur_marble = Marble(players_color, coord, i)
            if self.board.add_marble(cur_marble):
                i += 1
                continue

    def set_corner_to_player(self, corner_number: int, player: Union[LocalPlayer, ComputerPlayer]) -> None:
        """
        Setting a corner of the board for a given player, meaning that all the corner's coordinates will be filled
        with the player's marbles (according to their signature color).
        :param corner_number: int, one of the corners of the board
        :param player: local player or computer player
        :return: None
        """
        if corner_number == 1:
            self.set_coords_to_player(CORNER_1, player)
        elif corner_number == 2:
            self.set_coords_to_player(CORNER_2, player)
        elif corner_number == 3:
            self.set_coords_to_player(CORNER_3, player)
        elif corner_number == 4:
            self.set_coords_to_player(CORNER_4, player)
        elif corner_number == 5:
            self.set_coords_to_player(CORNER_5, player)
        elif corner_number == 6:
            self.set_coords_to_player(CORNER_6, player)

    def is_name_taken(self, name: str) -> bool:
        """
        Checks if a given name is already taken.
        :param name: str, name to check
        :return: True if it is already taken, False otherwise
        """
        for player in self.get_players_list():
            if player.get_name() == name:
                return True
        return False

    def is_color_taken(self, color: str) -> bool:
        """
        Checks if a given color is already taken.
        :param color: str, color to check
        :return: True if it is already taken, False otherwise
        """
        for player in self.__players_list:
            if player.get_color() == color:
                return True
        return False

    def new_local_player(self) -> None:
        """
        Creates a new local player. The user chooses a name and a color and when their valid the player will be
        created and added to the game.
        :return: None
        """
        while True:  # runs until user choose a valid name (shorter than 25 ,not taken and without ":" or ",")
            name = input("Choose your name: ")
            if len(name) > 25:
                print("Name is too long, please try again")
                playsound(helper.get_sound_path("invalid"))
                continue
            elif ":" in name or "," in name:
                print("the signs: , and : are not valid characters in name. Please try again")
                playsound(helper.get_sound_path("invalid"))
            elif self.is_name_taken(name):
                print("Name is already taken, please try again")
                playsound(helper.get_sound_path("invalid"))
                continue
            else:
                break
        while True:  # runs until user chose a valid color (in the VALID_COLORS list and not taken)
            color = input("Choose your color (R, B, G, P, C, Y): ").upper()
            if color not in VALID_COLORS:
                print("Invalid color, you can only choose from: R, B, G, P, C, Y. Please try again")
                playsound(helper.get_sound_path("invalid"))
                continue
            elif self.is_color_taken(color):
                print("Color is already taken, please pick another one")
                playsound(helper.get_sound_path("invalid"))
                continue
            else:
                break
        new_local_player = LocalPlayer(name, color)  # only when name and color are valid - the player is created
        self.add_player(new_local_player)

    def new_comp_player(self) -> None:
        """
        Creates a new computer player. randomly chooses a name and color out of a list and only if they are available.
        :return: None
        """
        comp_names = ["Leonardo", "Raphael", "Michelangelo", "Donatello", "Shredder", "Splinter"]
        # these are all the possible computer players name.
        while True:
            name = random.choice(comp_names)
            if not self.is_name_taken(name):
                break
        while True:
            color = random.choice(VALID_COLORS)
            if not self.is_color_taken(color):
                break
        new_comp_player = ComputerPlayer(name, color)
        self.add_player(new_comp_player)

    def add_all_players(self) -> None:
        """
        Creates and add all local and computer players.
        :return: None
        """
        comp_players_num = self.get_players_num() - self.get_local_players_num()  # number of computer players
        for local in range(self.get_local_players_num()):
            self.new_local_player()
        for comp in range(comp_players_num):
            self.new_comp_player()

    def set_board_for_2(self, players_list: List[Union[LocalPlayer, ComputerPlayer]]) -> None:
        """
        Sets up the board for a 2-player game by setting each player's marbles at a valid corner.
        :param players_list: list of all players of the game
        :return: None
        """
        i = 1
        for player in players_list:
            if i == 1:
                self.set_corner_to_player(1, player)
                player.set_corner_num(1)
            elif i == 2:
                self.set_corner_to_player(4, player)
                player.set_corner_num(4)
            i += 1

    def set_board_for_3(self, players_list: List[Union[LocalPlayer, ComputerPlayer]]) -> None:
        """
        Sets up the board for a game of 3 players by setting each player's marbles at a valid corner.
        :param players_list: list of all the players of the game
        :return: None
        """
        i = 1
        for player in players_list:
            if i == 1:
                self.set_corner_to_player(2, player)
                player.set_corner_num(2)
            elif i == 2:
                self.set_corner_to_player(4, player)
                player.set_corner_num(4)
            elif i == 3:
                self.set_corner_to_player(6, player)
                player.set_corner_num(6)
            i += 1

    def set_board_for_4(self, players_list: List[Union[LocalPlayer, ComputerPlayer]]) -> None:
        """
        Sets up the board for a game of 4 players by setting each player's marbles at a valid corner.
        :param players_list: list of all the players of the game
        :return: None
        """
        i = 1
        for player in players_list:
            if i == 1:
                self.set_corner_to_player(2, player)
                player.set_corner_num(2)
            elif i == 2:
                self.set_corner_to_player(3, player)
                player.set_corner_num(3)
            elif i == 3:
                self.set_corner_to_player(5, player)
                player.set_corner_num(5)
            elif i == 4:
                self.set_corner_to_player(6, player)
                player.set_corner_num(6)
            i += 1

    def set_board_for_6(self, players_list: List[Union[LocalPlayer, ComputerPlayer]]) -> None:
        """
        Sets up the board for a game of 6 players by setting each player's marbles at a valid corner.
        :param players_list: list of all the players of the game
        :return: None
        """
        i = 1
        for player in players_list:
            if i == 1:
                self.set_corner_to_player(1, player)
                player.set_corner_num(1)
            elif i == 2:
                self.set_corner_to_player(2, player)
                player.set_corner_num(2)
            elif i == 3:
                self.set_corner_to_player(3, player)
                player.set_corner_num(3)
            elif i == 4:
                self.set_corner_to_player(4, player)
                player.set_corner_num(4)
            elif i == 5:
                self.set_corner_to_player(5, player)
                player.set_corner_num(5)
            elif i == 6:
                self.set_corner_to_player(6, player)
                player.set_corner_num(6)
            i += 1

    def set_board(self, number_of_players: int) -> None:
        """
        Set the board according to the number of players that is given.
        :param number_of_players: int, number of players
        :return: None
        """
        players_list = self.get_players_list()
        if number_of_players == 2:
            self.set_board_for_2(players_list)
        elif number_of_players == 3:
            self.set_board_for_3(players_list)
        elif number_of_players == 4:
            self.set_board_for_4(players_list)
        elif number_of_players == 6:
            self.set_board_for_6(players_list)

    def new_game_settings(self) -> None:
        """
        Runs all the settings for a new game:
        choosing players number and how many are local, adding all players,
        creating new log file and setting the board.
        :return: None
        """
        total_players_num = helper.choose_players_num()  # how many players
        self.set_players_num(total_players_num)
        local_players_num = helper.choose_local_num(total_players_num)  # how many of them are local
        self.set_local_players_num(local_players_num)
        self.add_all_players()
        self.set_board(total_players_num)  # setting the board for the right number of players
        self.create_log_file()  # creates a new log for this game

    ####################################################################################
    # OLD GAME SETTINGS
    # all methods below are for settings for resuming an older game
    ####################################################################################

    def insert_players(self, players_info: List[List[str]]) -> None:
        """
        This function receives a list with players information and create them and add them to the game.
        The list contains inner lists for each player in the form of: [name, color, corner, wins, losses, type].
        :param players_info: list of players information
        :return: None
        """
        for player in players_info:
            if player[5] == "local":
                new_local_player = LocalPlayer(player[0], player[1], int(player[2]), int(player[3]), int(player[4]))
                self.add_player(new_local_player)
                self.set_players_num(self.get_players_num() + 1)
                self.set_local_players_num(self.get_local_players_num() + 1)
            elif player[5] == "computer":
                new_comp_player = ComputerPlayer(player[0], player[1], int(player[2]), int(player[3]), int(player[4]))
                self.add_player(new_comp_player)
                self.set_players_num(self.get_players_num() + 1)

    def insert_marbles(self, marbles_info: List[List[Any]]) -> None:
        """
        Inserts the marbles onto the board based on the provided informational list.
        The list contains inner lists for each marble in the form of: [color, coordinates, number]
        :param marbles_info: list of marbles info
        :return: None
        """
        for marble in marbles_info:
            color: str = marble[0]
            coords: Coordinates = marble[1]
            num: int = marble[2]
            new_marble = Marble(color, coords, num)
            self.board.add_marble(new_marble)

    def did_complete_round(self) -> bool:
        """
        Checks if the game completed full round or stopped in the middle of a round
        :return: True if the game completed full round, False otherwise
        """
        last_player = helper.last_played(self.get_log().get_log_path())
        return bool(last_player == self.get_players_list()[-1].get_name())

    def half_round(self) -> bool:
        """
        This function runs a "half-round" which means it allows continuation of the round from the last
        player who played.
        It will come to use when reloading an older game that ended mid-round.
        :return: None
        """
        print("round wasn't completed, let's continue from next player who didn't play")
        print(self.board)
        last_player_str = helper.last_played(self.get_log().get_log_path())
        for player in self.get_players_list():
            if last_player_str == player.get_name():  # finds last player who played
                last_player = player
            else:
                continue
        index = self.get_players_list().index(last_player)  # index of last played player
        for player in self.get_players_list():
            if self.get_players_list().index(player) <= index:  # if already played in round then we skip it
                continue
            else:  # for those who did not complete round there is a turn
                print(f"It's {player.get_name()}'s turn:  ")
                if isinstance(player, LocalPlayer):  # turn of a local player
                    details = self.turn_details(player, self.turn_of_local(player))  # run the turn and add info for log
                    self.get_log().add_to_log(details)
                    print(self.board)
                else:  # turn of a computer player
                    details = self.turn_details(player, self.turn_of_comp(player))  # run the turn and add info for log
                    self.get_log().add_to_log(details)
                    print(self.board)
                if self.board.check_player_won(player):
                    print(self.board)
                    self.update_wins_losses(player)
                    details = self.end_details(self.declare_winner(player))  # announce the winner and add info to log
                    self.get_log().add_to_log(details)
                    return False
                else:
                    continue
        return True

    def older_game_settings(self, game_choice: Tuple[str, str]) -> None:
        """
        This function sets the game to fit continuation of the chosen game:
        inserting the players and marbles as it was and updating the log to the old one.
        :param game_choice: tuple of strings: (path to file, game name)
        :return: None
        """
        players_info = helper.collect_players_info(game_choice[0])  # settings players
        self.insert_players(players_info)
        self.get_log().set_log_name(game_choice[1])  # resuming the older log
        if helper.is_there_board(game_choice[0]):
            marbles_info = helper.collect_marbles_info(game_choice[0])  # settings the board as it was
            self.insert_marbles(marbles_info)
        else:
            self.set_board(len(self.get_players_list()))  # this is in case the resumed game didn't start rounds

    ##############################################################################
    # LOG FILES
    # all methods bellow are log files related
    ##############################################################################

    def get_player_info(self) -> str:
        """
        This function gets the players information from the players list and returns it as a string.
        :return: string of the players info (name, color, corner, wins, losses, type)
        """
        players_list = self.get_players_list()
        players_info = ""
        for player in players_list:
            player_info = (f"Name: {player.get_name()}, Color: {player.get_color()}, Corner: {player.get_corner_num()},"
                           f" Wins: {player.get_wins()}, Losses: {player.get_losses()}, ")
            if isinstance(player, LocalPlayer):
                player_info += "Type: local"
            else:
                player_info += "Type: computer"
            players_info += player_info + "\n"
        return players_info

    def start_info(self) -> str:
        """
        This function arrange the game start information: players info and time of start.
        :return: string of the game start info
        """
        info = "\n" + "####################### GAME LOG #######################" + "\n"
        cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        info += "GAME START: " + cur_time + "\n"
        info += "PLAYERS INFO:" + "\n" + self.get_player_info()
        return info

    def create_log_file(self) -> None:
        """
        Creates a log file for the game
        :return: None
        """
        self.get_log().add_to_log(self.start_info())

    def continue_game_choice(self) -> bool:
        """
        Asks the user if they want to continue the game.
        :return: True if they want to continue, False otherwise
        """
        while True:
            answer = input("Do you want to get back to the game? (y/n) ")
            if answer == "y":
                print("BACK TO BUSINESS:", self.board, sep="\n")
                return True
            elif answer == "n":
                return False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    ##############################################################################
    # GAME RUN
    # All methods bellow are rounds related - running the game's turns
    ##############################################################################

    def hop_choice(self) -> bool:
        """
        Asks the player to choose step or hop with the marble.
        :return: True if player chose hop, False if chose step
        """
        while True:  # runs until decision is either step or jump
            decision = input("Would you rather step or hop?").lower()
            if decision == "step":
                return False
            elif decision == "hop":
                return True
            else:
                print("please choose 'step' or 'hop'.")
                playsound(helper.get_sound_path("invalid"))
                continue

    def another_hop_choice(self) -> bool:
        """
        Asks the player if they want to make another hop with the marble.
        :return: True if player chose another hop, False otherwise
        """
        print(self.board)
        while True:  # runs until decision is either Y or N
            decision = input("You can continue hopping. Another hop? (y/n) ")
            if decision.lower() == "n":
                return False
            elif decision.lower() == "y":
                return True
            else:
                print("Please enter 'y' or 'n'")
                playsound(helper.get_sound_path("invalid"))
                continue

    def local_one_hop(self, marble: Marble, loc_player: LocalPlayer) -> None:
        """
        Commits one hop of a given marble in the chosen direction. for a local player.
        :param marble: marble to move
        :param loc_player: local player that is playing
        :return: None
        """
        hop_options = self.board.marble_possible_hops(marble)
        while True:  # runs until player choose direction from possible hops list
            print("Your hop options are: ", *hop_options)
            chosen_hop_direction = loc_player.choose_direction()
            if chosen_hop_direction not in hop_options:
                print("Can't go there. Please try again")
                playsound(helper.get_sound_path("invalid"))
            else:
                break
        if self.board.hop_move_marble(marble, chosen_hop_direction):  # if successfully hopped
            return

    def local_hop_move(self, marble: Marble, loc_player: LocalPlayer) -> None:
        """
        Commits a hop move by player. runs until chosen hop's direction is valid.
        Also offers another hops if possible.
        :param marble: marble to move
        :param loc_player: player that playing
        :return: None
        """
        self.local_one_hop(marble, loc_player)
        playsound(helper.get_sound_path("hop"))
        while self.board.can_marble_hop(marble) and self.another_hop_choice():  # another hop offer if possible
            self.local_one_hop(marble, loc_player)
            playsound(helper.get_sound_path("hop"))
        else:
            return

    def local_step_move(self, marble: Marble, loc_player: LocalPlayer) -> None:
        """
        Commits a simple step move by player. runs until chosen step's direction is valid.
        :param marble: marble to move
        :param loc_player: player that playing
        :return: None
        """
        step_options = self.board.marble_possible_steps(marble)
        while True:  # runs until chosen direction is valid (in valid_directions and marble can move there)
            print("This marble's current step options are: ", *step_options)
            chosen_direction = loc_player.choose_direction()
            if chosen_direction not in step_options:
                print("Not a valid move. Please try again.")
                continue
            else:
                self.board.step_move_marble(marble, chosen_direction)
                return

    def comp_one_hop(self, marble: Marble) -> None:
        """
        Commits one hop of a given marble in the chosen direction. for a computer player.
        :param marble: marble to move
        :return: None
        """
        hop_options = self.board.marble_possible_hops(marble)
        chosen_direction = random.choice(hop_options)
        if self.board.hop_move_marble(marble, chosen_direction):
            return

    def comp_hop_move(self, marble: Marble, comp_player: ComputerPlayer) -> None:
        """
        Commits a hop move for a computer player. randomly chooses direction to hop and if to do another one.
        :param marble: marble to move
        :param comp_player: player that playing
        :return: None
        """
        self.comp_one_hop(marble)
        playsound(helper.get_sound_path("hop"))
        print(self.board)
        while self.board.can_marble_hop(marble) and comp_player.hop_choice():
            print(f"Another hop by {comp_player.get_name()}")
            self.comp_one_hop(marble)
            playsound(helper.get_sound_path("hop"))
            print(self.board)
        else:
            return

    def comp_step_move(self, marble: Marble) -> None:
        """
        Commits a simple step move by comp player. runs until chosen step's direction is valid.
        :param marble: marble to move
        :return: None
        """
        step_options = self.board.marble_possible_steps(marble)
        chosen_direction = random.choice(step_options)
        self.board.step_move_marble(marble, chosen_direction)
        return

    def valid_marble_for_local(self, loc_player: LocalPlayer) -> Marble:
        """
        Asks player to choose marble's number and runs until its valid - between 0 and 9.
        :param loc_player: player that playing
        :return: chosen marble
        """
        while True:  # runs until chosen number is valid (between 0 and 9 and can be moved)
            marble_num = loc_player.choose_marble()
            if marble_num == "logs":  # in case player asked to view older games
                chosen_game = helper.choose_game_to_read()
                helper.read_any_log(chosen_game[0])
                if self.continue_game_choice():
                    continue
                else:
                    print("ADIOS")
                    playsound(helper.get_sound_path("quit"))
                    quit()
            elif int(marble_num) < 0 or int(marble_num) > 9:  # checks number is valid
                print("Available marble numbers are between 0 and 9. Please try again")
                playsound(helper.get_sound_path("invalid"))
                continue
            chosen_marble_coord = self.board.convert_to_coords(loc_player, int(marble_num))  # converts to coordinates
            chosen_marble: Marble = self.board.game_board[chosen_marble_coord]
            if not self.board.can_marble_move(chosen_marble):  # checks if marble is movable
                print("This marble has no options to move. please pick another one.")
                playsound(helper.get_sound_path("invalid"))
                continue
            else:
                return chosen_marble

    def turn_of_local(self, loc_player: LocalPlayer) -> Union[List[Coordinates], str]:
        """
        Single turn of a local player:
        (If all the player's marbles are stuck then we skip this turn)
        1. Chooses marble
        2. If it can only hop, or it can hop and player chose to - then a hop move is done
        3. Else: a simple step move is done
        4. In each move the player chooses direction until the direction is valid
        :param loc_player: player whose turn to play
        :return: either a list or a string. if the player moved a marble then it will return a list of coordinates
        of the start location and the end location of the marble. otherwise, it will return "stuck"
        """
        if self.board.is_player_stuck(loc_player):  # if the player is stuck
            print("Oops, you're stuck for now ): maybe next round")
            playsound(helper.get_sound_path("stuck"))
            return "stuck"
        chosen_marble = self.valid_marble_for_local(loc_player)  # choose valid marble
        if (not self.board.can_marble_step(chosen_marble) or
                self.board.can_marble_hop(chosen_marble) and self.hop_choice()):
            # if marble can only hop, or it can hop and player chose to
            start_loc = chosen_marble.get_location()
            self.local_hop_move(chosen_marble, loc_player)
            finish_loc = chosen_marble.get_location()
            return [start_loc, finish_loc]
        else:  # step move
            start_loc = chosen_marble.get_location()
            self.local_step_move(chosen_marble, loc_player)
            playsound(helper.get_sound_path("step"))
            print(self.board)
            finish_loc = chosen_marble.get_location()
            return [start_loc, finish_loc]

    def valid_marble_for_comp(self, comp_player: ComputerPlayer) -> Marble:
        """
        Runs computer player marble choice until marble is valid.
        :param comp_player: player whose turn to play
        :return: chosen marble
        """
        players_marbles = self.board.list_player_marbles(comp_player)
        while True:
            chosen_marble_coord = comp_player.choose_marble(players_marbles)
            chosen_marble: Marble = self.board.game_board[chosen_marble_coord]
            if self.board.can_marble_move(chosen_marble):
                return chosen_marble
            else:
                continue

    def turn_of_comp(self, comp_player: ComputerPlayer) -> Union[List[Coordinates], str]:
        """
        Single turn of a computer player:
        (If all the player's marbles are stuck then we skip this turn)
        1. Movable marble is chosen randomly
        2. Hop or step is chosen randomly (if hopping is optional)
        3. Direction is chosen randomly
        :param comp_player: player whose turn to play
        :return: either a list or a string. if the player moved a marble then it will return a list of coordinates
        of the start location and the end location of the marble. otherwise, it will return "stuck"
        """
        if self.board.is_player_stuck(comp_player):  # if player is stuck we skip this turn
            return "stuck"
        chosen_marble = self.valid_marble_for_comp(comp_player)
        if (not self.board.can_marble_step(chosen_marble) or
                (self.board.can_marble_hop(chosen_marble) and comp_player.hop_choice())):  # hop option
            start_loc = chosen_marble.get_location()
            self.comp_hop_move(chosen_marble, comp_player)
            finish_loc = chosen_marble.get_location()
            return [start_loc, finish_loc]
        else:
            start_loc = chosen_marble.get_location()
            self.comp_step_move(chosen_marble)  # step move if not hop
            playsound(helper.get_sound_path("step"))
            print(self.board)
            finish_loc = chosen_marble.get_location()
            return [start_loc, finish_loc]

    def turn_details(self, player: Union[ComputerPlayer, LocalPlayer], movement: Union[List[Coordinates], str]) -> str:
        """
        Collect details about the current turn and return it as a string.
        :param player: player whose turn to play
        :param movement: list of coordinates of start and finish locations of the marble or the string "stuck"
        :return: string, containing details about the current turn
        """
        details = f"PLAYER: {player.get_name()} ({player.get_color()}) \n"
        details += "TIME: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        if movement == "stuck":
            details += f"MOVE: Player couldn't make a any moves.\n"
        else:
            details += f"MOVE: Player moved marble in location {movement[0]} to {movement[1]}.\n"
        details += "State of the board:" + "\n" + f"{self.board}" + "\n"
        details += self.marbles_details() + "\n"
        return details

    def marbles_details(self) -> str:
        """
        Returns a string with details about each marble. in the form of list for ech marble.
        Every list is of the form [color, coordinates, number].
        :return: string with details about all marbles
        """
        details = "Marbles state: " + "\n"
        for coord in self.board.game_board:
            if isinstance(self.board.game_board[coord], Marble):
                cur_marble = self.board.game_board[coord]
                details += f"[{cur_marble.get_color()} : {cur_marble.get_location()} : {cur_marble.get_number()}], "
        return details

    def end_details(self, player: Union[ComputerPlayer, LocalPlayer]) -> str:
        """
        Returns a string with the details of the game ending.
        :param player: The player who won the game
        :return: A string with the game ending details
        """
        details = f"{player.get_name()} has reached the opposite corner and won the game! \n"
        details += "End of game details: \n"
        details += f"WINNER: {player.get_name()} \n"
        details += f"players current status: \n"
        for player in self.get_players_list():
            details += f"{player.get_name()} - Wins: {player.get_wins()}, Losses: {player.get_losses()}\n"
        return details

    def declare_winner(self, player: Union[LocalPlayer, ComputerPlayer]) -> Union[LocalPlayer, ComputerPlayer]:
        """
        Prints and return the winner of the game.
        :param player: player who won
        :return: player who won
        """
        print(f"{player.get_name()} WINS THE GAME!!!")
        playsound(helper.get_sound_path("win2"))
        return player

    def update_wins_losses(self, winner: Union[LocalPlayer, ComputerPlayer]) -> None:
        """
        After a player has won, update the winning and losses of the players according to the results.
        :param winner: player who won
        :return: None
        """
        for player in self.get_players_list():
            if player is winner:
                player.add_win()
            else:
                player.add_loss()

    def one_round(self) -> bool:
        """
        One round of the game.
        Each player takes their turn and the board is displayed in between.
        If a player wins then the winner is declared.
        :return: True if no one wins, False otherwise
        """
        for player in self.get_players_list():
            print(f"It's {player.get_name()}'s turn:  ")
            if isinstance(player, LocalPlayer):  # turn of a local player
                details = self.turn_details(player, self.turn_of_local(player))  # run the turn and add info for log
                self.get_log().add_to_log(details)
            else:  # turn of a computer player
                details = self.turn_details(player, self.turn_of_comp(player))  # run the turn and add info for log
                self.get_log().add_to_log(details)
            if self.board.check_player_won(player):
                self.update_wins_losses(player)
                details = self.end_details(self.declare_winner(player))  # announce the winner and add info to log
                self.get_log().add_to_log(details)
                return False
            else:
                continue
        return True

    def another_game(self) -> bool:
        """
        Asks the user if they want to play again with those players
        :return: True if they want another game, False otherwise
        """
        while True:
            answer = input("Do you want to play another game with those players? (yes/no): ")
            if answer == "yes":
                return True
            elif answer == "no":
                return False
            else:
                print("Invalid answer, please try again.")
                playsound(helper.get_sound_path("invalid"))

    def reset_board_and_name(self) -> None:
        """
        Resets the board and name of the game. creates a new empty board and a new log object  for it.
        :return: None
        """
        self.board = Board()
        self.set_board(self.get_players_num())
        self.set_log()

    def play(self, half_round: bool = False) -> None:
        """
        Runs all the rounds of the game until the game ends, also offers another one when ended.
        :param half_round: this is only in case the older game resumed ended in the middle of the round.
        after finishing the "half round" (un-finished one) then the rounds continue normal.
        :return: None
        """
        if half_round:
            self.half_round()
        while True:
            print(f"Game number {self.get_log().get_log_name()[5:-4]}")
            print("GAME STARTED, GOOD LUCK!")
            print(self.board)
            playsound(helper.get_sound_path("new"))
            while True:
                if self.one_round():
                    continue
                else:
                    break
            print("GAME OVER")
            if self.another_game():  # another game with the same players offer
                self.reset_board_and_name()  # reset the board and make a new name for game
                continue
            else:
                break

    def run_game(self) -> None:
        """
        This function manage the flow of starting the game. it sets the game according to the user's choice
        of a new game or an older one, and then it runs the game.
        :return: None
        """
        while helper.load_older_option():  # player chose to resume an older game
            game_choice = helper.choose_game()
            helper.read_any_log(game_choice[0])
            if helper.resume_option():
                self.older_game_settings(game_choice)
                if not self.did_complete_round():  # in case older game ended mid round
                    playsound(helper.get_sound_path("back"))
                    self.play(half_round=True)
                else:
                    playsound(helper.get_sound_path("back"))
                    self.play()
            else:
                continue
        else:  # player chose to start a new game
            self.new_game_settings()
            self.play()
