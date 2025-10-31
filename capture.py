#################################################################
# FILE : capture.py
# WRITER : yael bar haim , yaelbarhaim , 315232132
# PROJECT : intro2cs final_project 2024
# DESCRIPTION: Capture class for "Chinese Checkers"
#################################################################


from playsound import playsound
import helper
from helper import Coordinates
from marble import Marble
from local_player import LocalPlayer
from computer_player import ComputerPlayer
from board import Board
from game import Game
import random
from typing import List, Union, Tuple, Dict


class Capture:
    """
    Represents a capture version game object - responsible for managing the flow of the game and its rules.
    Attributes: regular_game (Game) (used for its attributes and different method), captured_dict (dict) - a dictionary
    that stores the score of all players (by how many jumps they made = how many captures they did).
    Methods include: settings - adding all players and setting the board, running - managing the flow of the game.
    """

    def __init__(self) -> None:
        """
        A constructor for Capture object (capture version of the game)
        """
        self.game = Game()
        self.captured_dict: Dict[Union[LocalPlayer, ComputerPlayer], int] = {}

    def how_many_players(self) -> int:
        """
        Asks the user to enter how many players are playing.
        :return: int, total players number
        """
        while True:
            players_num = input("How many players are playing? (including computer players) ")
            if players_num == "2":
                return 2
            elif players_num == "3":
                return 3
            elif players_num == "4":
                return 4
            elif players_num == "5":
                return 5
            elif players_num == "6":
                return 6
            else:
                print("Number of players can only be between 1 to 6. Please try again.")
                playsound(helper.get_sound_path("invalid"))
                continue

    def how_many_local_players(self) -> int:
        """
        Asks the user to enter how many local players are playing.
        :return: int, local players number
        """
        while True:
            players_num = input("How many local players are playing? (the rest will be computer players) ")
            if players_num == "1":
                return 1
            elif players_num == "2":
                return 2
            elif players_num == "3":
                return 3
            elif players_num == "4":
                return 4
            elif players_num == "5":
                return 5
            elif players_num == "6":
                return 6
            else:
                print("Number of players can only be between 1 to 6. Please try again.")
                playsound(helper.get_sound_path("invalid"))
                continue

    def update_players_numbers(self) -> None:
        """
        Updates the players numbers based on the user choices.
        :return: None
        """
        total_players = self.how_many_players()
        local_players = self.how_many_local_players()
        self.game.set_players_num(total_players)
        self.game.set_local_players_num(local_players)

    def new_local_player_capture(self) -> None:
        """
        Creates a new local player. The user chooses a name until valid.
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
            elif self.game.is_name_taken(name):
                print("Name is already taken, please try again")
                playsound(helper.get_sound_path("invalid"))
                continue
            else:
                break
        new_local_player = LocalPlayer(name, "P")   # creates new local player (color is irrelevant)
        self.game.add_player(new_local_player)    # adds the player
        self.captured_dict[new_local_player] = 0  # updates their score to 0

    def new_comp_player_capture(self) -> None:
        """
        Creates a new computer player. randomly chooses a name out of a list and only if it's available.
        :return: None
        """
        comp_names = ["Leonardo", "Raphael", "Michelangelo", "Donatello", "Shredder", "Splinter"]
        # these are all the possible computer players name.
        while True:
            name = random.choice(comp_names)
            if not self.game.is_name_taken(name):
                break
        new_comp_player = ComputerPlayer(name, "P")   # creates new comp player (color is irrelevant)
        self.game.add_player(new_comp_player)    # adds the player
        self.captured_dict[new_comp_player] = 0  # updates their score to 0

    def add_all_players(self) -> None:
        """
        Adds all players to the game.
        :return: None
        """
        self.update_players_numbers()
        local_num = self.game.get_local_players_num()
        comps_num = self.game.get_players_num() - local_num
        for local_player in range(local_num):
            self.new_local_player_capture()
        for comp_player in range(comps_num):
            self.new_comp_player_capture()

    def get_starting_coords(self) -> List[Coordinates]:
        """
        This function is used to get a list of all the coordinates where marbles are set at the beginning.
        :return: list of coordinates
        """
        start_coords = []
        for coord in self.game.board.game_board:
            if coord in helper.CORNER_1:
                continue
            elif coord in helper.CORNER_2:
                continue
            elif coord in helper.CORNER_3:
                continue
            elif coord in helper.CORNER_4:
                continue
            elif coord in helper.CORNER_5:
                continue
            elif coord in helper.CORNER_6:
                continue
            elif coord == (8, 12):
                continue
            else:
                start_coords.append(coord)
        return start_coords

    def set_board_capture(self) -> None:
        """
        This method sets the board to a game of capture.
        Placing marbles all over except for the very middle and the corners.
        :return: None
        """
        start_coords = self.get_starting_coords()
        index = 0
        for color in helper.VALID_COLORS:
            for num in range(0, 10):
                new_loc = start_coords[index]
                new_marble = Marble(color, new_loc, num)
                self.game.board.add_marble(new_marble)
                index += 1

    def list_possible_marbles(self) -> List[Marble]:
        """
        This method list all the marbles that are on the board and can hop
        :return: list of marbles that can be chosen
        """
        possible_marbles: List[Marble] = []
        for coord in self.game.board.game_board:
            content = self.game.board.game_board[coord]
            if isinstance(content, Marble) and self.game.board.can_marble_hop(content):
                possible_marbles.append(content)
            else:
                continue
        return possible_marbles

    def get_specific_marble(self, marble_info: Tuple[str, int]) -> Marble:
        """
        This method gets the marble of a given color and a given number
        :param marble_info: tuple of first letter of the color followed by a number
        :return: marble on the given coordinates
        """
        for coord in self.game.board.game_board:
            content = self.game.board.game_board[coord]
            if isinstance(content, Marble):
                if content.get_color() == marble_info[0] and content.get_number() == marble_info[1]:
                    return content
                else:
                    continue
            else:
                continue
        return Marble(marble_info[0], (0, 0), marble_info[1])  # not on board, for return value

    def local_choose_marble(self) -> Marble:
        """
        Asks the user to choose a marble to move. Runs until input is valid: first letter of the color followed by a
        number when both are from the valid options.
        An example of a valid input: G4 (green number 4).
        :return: chosen marble
        """
        while True:
            chosen_marble = input("Please enter marble to move: ")
            if chosen_marble == "quit":
                print("ADIOS")
                playsound(helper.get_sound_path("quit"))
                quit()
            if len(chosen_marble) != 2:  # validates length
                print("You must enter one letter and one number (first letter of color followed by number. Ex: G4).")
                playsound(helper.get_sound_path("invalid"))
            elif chosen_marble[0].upper() not in helper.VALID_COLORS:  # validates color
                print("You must enter one letter and one number (first letter of color followed by number. Ex: G4).")
                playsound(helper.get_sound_path("invalid"))
            elif chosen_marble[1] not in "0123456789":   # validates number
                print("You must enter one letter and one number (first letter of color followed by number. Ex: G4).")
                playsound(helper.get_sound_path("invalid"))
            else:
                marble_info = chosen_marble[0].upper(), int(chosen_marble[1])
                marble = self.get_specific_marble(marble_info)
                if marble not in self.list_possible_marbles():   # checks if on-board and can hop
                    print("You must pick a marble that is ON THE BOARD and CAN HOP. Please try again.")
                    playsound(helper.get_sound_path("invalid"))
                    continue
                else:
                    return marble

    def comp_choose_marble(self) -> Marble:
        """
        Randomly chooses a marble for the computer player to move.
        :return: chosen marble
        """
        return random.choice(self.list_possible_marbles())

    def local_choose_direction(self, chosen_marble: Marble) -> str:
        """
        Asks the user to choose the direction to move the marble to. runs until direction is valid
        :param chosen_marble: marble to move
        :return: str, chosen direction
        """
        hop_options = self.game.board.marble_possible_hops(chosen_marble)
        while True:
            print("Your hop options are: ", *hop_options)
            direction = input(f"Enter hopping direction: ")
            if direction.lower() not in hop_options:
                print("Invalid direction. Please try again.")
                playsound(helper.get_sound_path("invalid"))
            else:
                return direction.lower()

    def comp_choose_direction(self, chosen_marble: Marble) -> str:
        """
        randomly chooses a direction for the computer player to move the marble to, out of possible directions.
        :param chosen_marble: marble to move
        :return: str, chosen direction
        """
        possible_directions = self.game.board.marble_possible_hops(chosen_marble)
        return random.choice(possible_directions)

    def add_point_to_player(self, player: Union[LocalPlayer, ComputerPlayer]) -> None:
        """
        Adds a point to the player.
        :param player: player to add the point to
        :return: None
        """
        self.captured_dict[player] += 1

    def marble_one_hop(self, player: Union[LocalPlayer, ComputerPlayer], marble: Marble, direction: str) -> None:
        """
        Move a given marble by hop one time to a given direction. removes the marble that is hopped over,
        and adds one point to the player that is currently playing.
        :param player: player who plays
        :param marble: marble to move
        :param direction: direction to move the marble to
        :return: None
        """
        current_coord = marble.get_location()
        cur_row, cur_col = current_coord
        hopped_over_coord = marble.step_requirements(direction)
        over_row, over_col = hopped_over_coord
        hopped_to_coord = marble.hop_requirements(direction)
        new_row, new_col = hopped_to_coord
        self.game.board.game_board[hopped_to_coord] = marble
        self.game.board.visual_board[new_row][new_col] = marble.get_color()[0]
        self.game.board.game_board[current_coord] = 0   # empty previous location of marble
        self.game.board.visual_board[cur_row][cur_col] = 1
        self.game.board.game_board[hopped_over_coord] = 0  # removes marble hoped over
        self.game.board.visual_board[over_row][over_col] = 1
        marble.set_location(hopped_to_coord)  # update marble's location
        self.add_point_to_player(player)  # add point for player
        print(self.game.board)
        playsound(helper.get_sound_path("hop"))

    def local_turn(self, player: LocalPlayer) -> None:
        """
        This method runs the turn of a local player: choose marble, choose direction, moves the marble and updates
        everything, lastly offers another hop if possible.
        :param player: local player that plays
        :return: None
        """
        chosen_marble = self.local_choose_marble()
        chosen_direction = self.local_choose_direction(chosen_marble)
        self.marble_one_hop(player, chosen_marble, chosen_direction)  # first hop
        while self.game.board.can_marble_hop(chosen_marble) and self.game.another_hop_choice():  # another hop option
            print("another hop:")
            chosen_direction = self.local_choose_direction(chosen_marble)
            self.marble_one_hop(player, chosen_marble, chosen_direction)

    def comp_turn(self, player: ComputerPlayer) -> None:
        """
        This method runs the turn of a computer player: choose marble, choose direction, moves the marble and updates
        everything, lastly offers another hop if possible.
        :param player: computer player that plays
        :return: None
        """
        chosen_marble = self.comp_choose_marble()
        chosen_direction = self.comp_choose_direction(chosen_marble)
        self.marble_one_hop(player, chosen_marble, chosen_direction)   # first hop
        while self.game.board.can_marble_hop(chosen_marble) and player.hop_choice():  # another hop option
            print(f"{player.get_name()}'s another hop:")
            chosen_direction = self.comp_choose_direction(chosen_marble)
            self.marble_one_hop(player, chosen_marble, chosen_direction)

    def print_score(self) -> None:
        """
        This method prints the current score of the game
        :return: None
        """
        status = "Current Score:\n"
        for player, score in self.captured_dict.items():
            status += f"{player.get_name()}: {score}, "
        print(status)

    def is_game_over(self) -> bool:
        """
        This method checks if the game is over.
        :return: True if game is over, False otherwise
        """
        return not bool(self.list_possible_marbles())

    def get_winner(self) -> Union[LocalPlayer, ComputerPlayer]:
        """
        This method returns the winner of the game by choosing the player with the highest
         score in the captured dictionary.
        :return: local player or computer player who has the highest score
        """
        captured_count = self.captured_dict
        return max(captured_count, key=captured_count.get)

    def one_round_capture(self) -> bool:
        """
        One round of the game.
        Each player takes their turn and the board is displayed in between.
        If a player wins then the winner is declared.
        :return: True if no one wins, False otherwise
        """
        for player in self.game.get_players_list():
            print(f"It's {player.get_name()}'s turn:  ")
            if isinstance(player, LocalPlayer):  # turn of a local player
                self.local_turn(player)
            else:  # turn of a computer player
                self.comp_turn(player)
            if self.is_game_over():  # checks if the game is over
                winner = self.get_winner()  # finds the winner
                won = self.game.declare_winner(winner)  # announcing the winner
                self.game.update_wins_losses(won)  # updates wins and losses
                return False
            else:
                self.print_score()
                continue
        return True

    def reset_game(self) -> None:
        """
        This method resets the game: resets the board and set it up as in the beginning, keep the players but reset
        all the captured scores in the captured dictionary.
        :return: None
        """
        self.game.board = Board()
        self.set_board_capture()
        for player in self.game.get_players_list():
            self.captured_dict[player] = 0

    def play_capture(self) -> None:
        """
        Runs all the rounds of the game until the game ends, also offers another one when ended.
        :return: None
        """
        self.add_all_players()    # set players
        self.set_board_capture()  # set board
        while True:   # starts game
            print("GAME STARTED, GOOD LUCK!")
            print(self.game.board)
            playsound(helper.get_sound_path("new"))
            while True:
                if self.one_round_capture():
                    continue
                else:
                    break
            print("GAME OVER")
            if self.game.another_game():  # another game with the same players offer
                self.reset_game()  # reset the board and make a new name for game
                continue
            else:
                break
