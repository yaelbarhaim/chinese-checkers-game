from board import Board
from marble import Marble
from computer_player import ComputerPlayer
from local_player import LocalPlayer
from game import Game
from helper import *
from typing import Tuple


def test_board_init() -> None:
    board1 = Board()
    assert isinstance(board1.visual_board, list)
    assert isinstance(board1.game_board, dict)
    assert len(board1.visual_board) == 17  # Check board dimensions
    assert len(board1.visual_board[0]) == 25  # Check board dimensions


def test_board_str() -> None:
    board1 = Board
    assert isinstance(str(board1), str)


def test_is_coord_empty() -> None:
    board1 = Board()
    assert board1.is_coord_empty((0, 12))
    marble = Marble("R", (0, 12), 1)
    board1.add_marble(marble)
    assert not board1.is_coord_empty((0, 12))
    assert board1.is_coord_empty((3, 13))


def test_is_coord_on_board() -> None:
    board1 = Board()
    assert board1.is_coord_on_board((3, 11))
    assert board1.is_coord_on_board((4, 6))
    assert board1.is_coord_on_board((4, 12))
    assert board1.is_coord_on_board((6, 4))
    assert board1.is_coord_on_board((5, 19))
    assert board1.is_coord_on_board((10, 16))
    assert not board1.is_coord_on_board((0, 0))
    assert not board1.is_coord_on_board((1, 0))
    assert not board1.is_coord_on_board((16, 24))
    assert not board1.is_coord_on_board((4, 7))
    assert not board1.is_coord_on_board((3, 8))
    assert not board1.is_coord_on_board((0, -1))
    assert not board1.is_coord_on_board((0, 25))
    assert not board1.is_coord_on_board((17, 0))
    assert not board1.is_coord_on_board((-17, 25))
    assert not board1.is_coord_on_board((-1, -1))
    assert not board1.is_coord_on_board((17, 25))
    assert not board1.is_coord_on_board((0, 25))
    assert not board1.is_coord_on_board((17, 0))


def test_add_marble() -> None:
    board1 = Board()
    marble1 = Marble("R", (0, 12), 1)  # Creating a sample marble
    assert board1.add_marble(marble1)
    assert not board1.add_marble(marble1)  # Adding the same marble again should fail
    assert board1.visual_board[0][12] == "R"  # Check if the marble is correctly added to the visual board
    assert board1.game_board[(0, 12)] == marble1
    marble2 = Marble("B", (0, 12), 1)
    assert not board1.add_marble(marble2)  # Adding a marble to an occupied coordinate should fail
    marble3 = Marble("B", (-1, -1), 1)
    assert not board1.add_marble(marble3)  # Adding a marble to an invalid coordinate should fail
    marble4 = Marble("B", (1, 11), 1)
    assert board1.add_marble(marble4)
    marble5 = Marble("B", (0, 0), 7)
    assert not board1.add_marble(marble5)
    marble6 = Marble("KK", (2, 14), 3)  # should work for wierd color as well
    assert board1.add_marble(marble6)
    marble7 = Marble("C", (4, 6), 20)   # should work for later-invalid marble number
    assert board1.add_marble(marble7)


def test_step_move_marble() -> None:
    board1 = Board()
    marble1 = Marble("R", (5, 11), 1)  # Creating a sample marble
    board1.add_marble(marble1)  # Adding the marble to the board
    assert board1.step_move_marble(marble1, "ul")
    assert board1.game_board[(0, 12)] == 0  # The previous position of the marble should be empty in the game board
    assert board1.step_move_marble(marble1, "dr")
    assert board1.step_move_marble(marble1, "ur")
    assert board1.game_board[(0, 12)] == 0
    assert board1.step_move_marble(marble1, "dl")
    assert board1.step_move_marble(marble1, "jl")
    assert board1.step_move_marble(marble1, "jr")
    marble2 = Marble("B", (0, 12), 5)
    marble3 = Marble("C", (1, 11), 4)
    marble4 = Marble("B", (1, 13), 2)
    marble5 = Marble("B", (2, 10), 5)
    marble6 = Marble("C", (2, 12), 4)
    marble7 = Marble("B", (2, 14), 2)
    board1.add_marble(marble2)
    board1.add_marble(marble3)
    board1.add_marble(marble4)
    board1.add_marble(marble5)
    board1.add_marble(marble6)
    board1.add_marble(marble7)
    assert not board1.step_move_marble(marble4, "ul")
    assert not board1.step_move_marble(marble4, "dl")
    assert not board1.step_move_marble(marble4, "ur")
    assert not board1.step_move_marble(marble4, "dr")
    assert not board1.step_move_marble(marble4, "jl")
    assert not board1.step_move_marble(marble4, "jr")
    assert not board1.step_move_marble(marble2, "ul")
    assert not board1.step_move_marble(marble2, "ur")
    assert not board1.step_move_marble(marble2, "dl")
    assert not board1.step_move_marble(marble2, "dr")
    assert not board1.step_move_marble(marble2, "jl")
    assert not board1.step_move_marble(marble2, "jr")


def test_hop_move_marble() -> None:
    board5 = Board()
    marble1 = Marble("R", (5, 11), 1)  # Creating a sample marble
    board5.add_marble(marble1)  # Adding the marble to the board
    assert not board5.hop_move_marble(marble1, "ul")
    assert not board5.hop_move_marble(marble1, "dl")
    assert not board5.hop_move_marble(marble1, "ur")
    assert not board5.hop_move_marble(marble1, "dr")
    assert not board5.hop_move_marble(marble1, "jl")
    assert not board5.hop_move_marble(marble1, "jr")
    assert not board5.hop_move_marble(marble1, "Qs")
    assert not board5.hop_move_marble(marble1, "kk")
    assert not board5.hop_move_marble(marble1, "right")
    marble2 = Marble("B", (0, 12), 5)
    marble3 = Marble("C", (1, 11), 4)
    marble4 = Marble("B", (1, 13), 2)
    marble5 = Marble("B", (2, 10), 5)
    marble6 = Marble("C", (2, 12), 4)
    marble7 = Marble("B", (2, 14), 2)
    board5.add_marble(marble2)
    board5.add_marble(marble3)
    board5.add_marble(marble4)
    board5.add_marble(marble5)
    board5.add_marble(marble6)
    board5.add_marble(marble7)
    assert board5.hop_move_marble(marble3, "dl")
    assert board5.game_board[(1, 11)] == 0  # should now be empty
    assert board5.hop_move_marble(marble3, "ur")
    assert board5.game_board[(1, 11)] == marble3  # got back
    assert not board5.hop_move_marble(marble2, "ul")
    assert not board5.hop_move_marble(marble2, "ur")
    assert not board5.hop_move_marble(marble2, "dl")
    assert not board5.hop_move_marble(marble2, "dr")
    assert not board5.hop_move_marble(marble2, "jl")
    assert not board5.hop_move_marble(marble2, "jr")
    board4 = Board()
    marble1 = Marble("R", (8, 16), 1)
    marble2 = Marble("R", (7, 15), 1)
    marble3 = Marble("R", (7, 17), 1)
    marble4 = Marble("R", (9, 15), 1)
    marble5 = Marble("R", (9, 17), 1)
    marble6 = Marble("R", (8, 14), 1)
    marble7 = Marble("R", (8, 18), 1)
    board4.add_marble(marble1)
    board4.add_marble(marble2)
    board4.add_marble(marble3)
    board4.add_marble(marble4)
    board4.add_marble(marble5)
    board4.add_marble(marble6)
    board4.add_marble(marble7)
    assert board4.hop_move_marble(marble1, "dr")
    assert board4.hop_move_marble(marble1, "ul")
    assert board4.hop_move_marble(marble1, "dl")
    assert board4.hop_move_marble(marble1, "ur")
    assert board4.hop_move_marble(marble1, "jr")
    assert board4.hop_move_marble(marble1, "jl")


def test_marble_possible_steps() -> None:
    board = Board()
    marble1 = Marble("R", (0, 12), 1)  # Creating a sample marble
    board.add_marble(marble1)  # Adding the marble to the board
    assert board.marble_possible_steps(marble1) == ["dl", "dr"]
    marble2 = Marble("B", (5, 11), 7)
    board.add_marble(marble2)
    assert board.marble_possible_steps(marble2) == ["ul", "ur", "dl", "dr", "jl", "jr"]
    marble8 = Marble("R", (16, 12), 2)
    board.add_marble(marble8)
    assert board.marble_possible_steps(marble8) == ["ul", "ur"]


def test_marble_possible_hops() -> None:
    board = Board()
    marble = Marble("R", (0, 12), 1)  # Creating a sample marble
    marble3 = Marble("C", (1, 11), 4)
    marble4 = Marble("B", (1, 13), 2)
    marble5 = Marble("B", (2, 10), 5)
    marble6 = Marble("C", (2, 12), 4)
    marble7 = Marble("B", (2, 14), 2)
    board.add_marble(marble)  # Adding the marble to the board
    board.add_marble(marble3)
    board.add_marble(marble4)
    board.add_marble(marble5)
    board.add_marble(marble6)
    board.add_marble(marble7)
    assert board.marble_possible_hops(marble) == []
    assert board.marble_possible_hops(marble3) == ["dl", "dr"]
    assert board.marble_possible_hops(marble4) == ["dl", "dr"]
    assert board.marble_possible_hops(marble5) == []
    assert board.marble_possible_hops(marble6) == []
    assert board.marble_possible_hops(marble7) == []
    board4 = Board()
    marble1 = Marble("R", (8, 16), 1)
    marble2 = Marble("R", (7, 15), 1)
    marble3 = Marble("R", (7, 17), 1)
    marble4 = Marble("R", (9, 15), 1)
    marble5 = Marble("R", (9, 17), 1)
    marble6 = Marble("R", (8, 14), 1)
    marble7 = Marble("R", (8, 18), 1)
    board4.add_marble(marble1)
    board4.add_marble(marble2)
    board4.add_marble(marble3)
    board4.add_marble(marble4)
    board4.add_marble(marble5)
    board4.add_marble(marble6)
    board4.add_marble(marble7)
    assert board4.marble_possible_hops(marble1) == VALID_DIRECTIONS


def test_can_marble_step() -> None:
    board = Board()
    marble2 = Marble("R", (0, 12), 1)  # Creating a sample marble
    marble3 = Marble("C", (1, 11), 4)
    marble4 = Marble("B", (1, 13), 2)
    marble5 = Marble("B", (2, 10), 5)
    marble6 = Marble("C", (2, 12), 4)
    marble7 = Marble("B", (2, 14), 2)
    board.add_marble(marble2)  # Adding the marble to the board
    board.add_marble(marble3)
    board.add_marble(marble4)
    board.add_marble(marble5)
    board.add_marble(marble6)
    board.add_marble(marble7)
    assert not board.can_marble_step(marble2)
    assert not board.can_marble_step(marble3)
    assert not board.can_marble_step(marble4)
    assert board.can_marble_step(marble5)
    assert board.can_marble_step(marble6)
    assert board.can_marble_step(marble7)


def test_can_marble_hop() -> None:
    board = Board()
    marble2 = Marble("R", (0, 12), 1)  # Creating sample marbles
    marble3 = Marble("C", (1, 11), 4)
    marble4 = Marble("B", (1, 13), 2)
    marble5 = Marble("B", (2, 10), 5)
    marble6 = Marble("C", (2, 12), 4)
    marble7 = Marble("B", (2, 14), 2)
    board.add_marble(marble2)  # Adding the marbles to the board
    board.add_marble(marble3)
    board.add_marble(marble4)
    board.add_marble(marble5)
    board.add_marble(marble6)
    board.add_marble(marble7)
    assert not board.can_marble_hop(marble2)
    assert board.can_marble_hop(marble3)
    assert board.can_marble_hop(marble4)
    assert not board.can_marble_hop(marble5)
    assert not board.can_marble_hop(marble6)
    assert not board.can_marble_hop(marble7)


def test_can_marble_move() -> None:
    board = Board()
    marble2 = Marble("R", (0, 12), 1)  # Creating sample marbles
    marble3 = Marble("C", (1, 11), 4)
    marble4 = Marble("B", (1, 13), 2)
    marble5 = Marble("B", (2, 10), 5)
    marble6 = Marble("C", (2, 12), 4)
    marble7 = Marble("B", (2, 14), 2)
    board.add_marble(marble2)  # Adding the marbles to the board
    board.add_marble(marble3)
    board.add_marble(marble4)
    board.add_marble(marble5)
    board.add_marble(marble6)
    board.add_marble(marble7)
    assert not board.can_marble_move(marble2)
    assert board.can_marble_move(marble3)
    assert board.can_marble_move(marble4)
    assert board.can_marble_move(marble5)
    assert board.can_marble_move(marble6)
    assert board.can_marble_move(marble7)


def test_list_player_marbles() -> None:
    game = Game()
    game.set_players_num(2)
    game.set_local_players_num(1)
    player1 = LocalPlayer("Ruth", "Y")
    player2 = ComputerPlayer("Bader", "C")
    game.add_player(player1)
    game.add_player(player2)
    marble1 = Marble("Y", (0, 12), 7)
    marble2 = Marble("Y", (4, 6), 9)
    marble3 = Marble("C", (2, 14), 7)
    game.board.add_marble(marble1)
    game.board.add_marble(marble2)
    game.board.add_marble(marble3)
    assert isinstance(game.board.list_player_marbles(player1), list)
    assert isinstance(game.board.list_player_marbles(player2), list)
    assert game.board.list_player_marbles(player1) == [(0, 12), (4, 6)]
    assert game.board.list_player_marbles(player2) == [(2, 14)]


def test_is_player_stuck() -> None:
    game = Game()
    game.set_players_num(2)
    game.set_local_players_num(1)
    player1 = LocalPlayer("Ruth", "Y")
    player2 = ComputerPlayer("Bader", "C")
    game.add_player(player1)
    game.add_player(player2)
    marble1 = Marble("Y", (0, 12), 7)
    marble2 = Marble("C", (1, 11), 9)
    marble3 = Marble("C", (1, 13), 7)
    marble4 = Marble("C", (2, 10), 2)
    marble5 = Marble("C", (2, 12), 3)
    marble6 = Marble("C", (2, 14), 5)
    game.board.add_marble(marble1)
    game.board.add_marble(marble2)
    game.board.add_marble(marble3)
    game.board.add_marble(marble4)
    game.board.add_marble(marble5)
    game.board.add_marble(marble6)
    assert game.board.is_player_stuck(player1)
    assert not game.board.is_player_stuck(player2)


def test_get_corner_coords() -> None:
    board = Board()
    assert board.get_corner_coords(1) == CORNER_1
    assert board.get_corner_coords(2) == CORNER_2
    assert board.get_corner_coords(3) == CORNER_3
    assert board.get_corner_coords(4) == CORNER_4
    assert board.get_corner_coords(5) == CORNER_5
    assert board.get_corner_coords(6) == CORNER_6


def test_get_target_corner() -> None:
    player1 = LocalPlayer("Ruth", "Y", 1)
    player2 = ComputerPlayer("Bader", "C", 2)
    player3 = LocalPlayer("John", "R", 3)
    player4 = ComputerPlayer("Jane", "B", 4)
    player5 = LocalPlayer("Mike", "G", 5)
    player6 = ComputerPlayer("Sarah", "M", 6)
    game = Game()
    game.set_players_num(6)
    game.set_local_players_num(3)
    game.add_player(player1)
    game.add_player(player2)
    game.add_player(player3)
    game.add_player(player4)
    game.add_player(player5)
    game.add_player(player6)
    assert game.board.get_target_corner(player1) == 4
    assert game.board.get_target_corner(player2) == 5
    assert game.board.get_target_corner(player3) == 6
    assert game.board.get_target_corner(player4) == 1
    assert game.board.get_target_corner(player5) == 2
    assert game.board.get_target_corner(player6) == 3


def test_check_player_won() -> None:
    board = Board()
    player1 = LocalPlayer("Ruth", "Y", 1)
    player2 = ComputerPlayer("Bader", "C", 2)
    player3 = LocalPlayer("John", "R", 3)
    game = Game()
    game.set_players_num(3)
    game.set_local_players_num(2)
    game.add_player(player1)
    game.add_player(player2)
    game.add_player(player3)
    for i in range(10):
        coord = CORNER_4[i]
        new_marble = Marble("Y", coord, i)
        board.add_marble(new_marble)
    marble1 = Marble("C", (0, 12), 3)
    board.add_marble(marble1)
    marble2 = Marble("R", (4, 14), 3)
    board.add_marble(marble2)
    assert board.check_player_won(player1)
    assert not board.check_player_won(player2)
    assert not board.check_player_won(player3)


def test_convert_to_coords() -> None:
    player1 = LocalPlayer("Ruth", "Y", 1)
    player2 = LocalPlayer("Bader", "C", 2)
    player3 = LocalPlayer("John", "R", 3)
    game = Game()
    game.set_players_num(3)
    game.set_local_players_num(3)
    game.add_player(player1)
    game.add_player(player2)
    game.add_player(player3)
    for i in range(10):
        coord = CORNER_4[i]
        new_marble = Marble("Y", coord, i)
        game.board.add_marble(new_marble)
    marble1 = Marble("C", (0, 12), 3)
    game.board.add_marble(marble1)
    marble2 = Marble("R", (4, 14), 3)
    game.board.add_marble(marble2)
    assert isinstance(game.board.convert_to_coords(player1, 1), Tuple)
    assert game.board.convert_to_coords(player1, 0) == (13, 9)
    assert game.board.convert_to_coords(player1, 1) == (13, 11)
    assert game.board.convert_to_coords(player2, 3) == (0, 12)
    assert game.board.convert_to_coords(player3, 3) == (4, 14)

