from game import Game
from local_player import LocalPlayer
from computer_player import ComputerPlayer
from board import Board
from helper import *
from log import Log
import os


def test_game_init() -> None:
    game = Game()
    assert isinstance(game, Game)
    assert game.get_players_num() == 0
    assert game.get_local_players_num() == 0
    assert game.get_players_list() == []
    assert isinstance(game.get_log(), Log)


def test_get_players_and_local_num() -> None:
    game = Game()
    game.set_players_num(4)
    game.set_local_players_num(2)
    assert game.get_players_num() == 4
    assert game.get_local_players_num() == 2
    game.set_players_num(3)
    game.set_local_players_num(1)
    assert game.get_players_num() == 3
    assert game.get_local_players_num() == 1
    game.set_players_num(2)
    game.set_local_players_num(2)
    assert game.get_players_num() == 2
    assert game.get_local_players_num() == 2


def test_set_players_and_local_num() -> None:
    game = Game()
    game.set_players_num(6)
    game.set_local_players_num(1)
    assert game.get_players_num() == 6
    assert game.get_local_players_num() == 1
    game.set_players_num(2)
    game.set_local_players_num(2)
    assert game.get_players_num() == 2
    assert game.get_local_players_num() == 2
    game.set_players_num(4)
    game.set_local_players_num(3)
    assert game.get_players_num() == 4
    assert game.get_local_players_num() == 3


def test_get_players_list() -> None:
    game = Game()
    game.set_players_num(6)
    game.set_local_players_num(4)
    assert game.get_players_list() == []
    player1 = LocalPlayer("Player1", "R")
    player2 = LocalPlayer("Player2", "B")
    player3 = LocalPlayer("Player3", "W")
    player4 = LocalPlayer("Player4", "K")
    player5 = ComputerPlayer("Player5", "G")
    player6 = ComputerPlayer("Player6", "H")
    game.add_player(player1)
    assert game.get_players_list() == [player1]
    game.add_player(player2)
    assert game.get_players_list() == [player1, player2]
    game.add_player(player3)
    assert game.get_players_list() == [player1, player2, player3]
    game.add_player(player4)
    assert game.get_players_list() == [player1, player2, player3, player4]
    game.add_player(player5)
    assert game.get_players_list() == [player1, player2, player3, player4, player5]
    game.add_player(player6)
    assert game.get_players_list() == [player1, player2, player3, player4, player5, player6]


def test_get_log() -> None:
    game = Game()
    assert isinstance(game.get_log(), Log)
    assert isinstance(game.get_log().get_log_path(), str)
    assert isinstance(game.get_log().get_log_name(), str)


def test_set_log() -> None:
    game = Game()
    game.set_log()
    new_log = game.get_log()
    assert isinstance(new_log, Log)
    assert isinstance(new_log.get_log_path(), str)
    assert isinstance(new_log.get_log_name(), str)


def test_add_player() -> None:
    game = Game()
    game.set_players_num(4)
    game.set_local_players_num(2)
    player = LocalPlayer("Test Player", "R")
    game.add_player(player)
    assert len(game.get_players_list()) == 1
    assert player in game.get_players_list()
    player2 = ComputerPlayer("Test again", "Y")
    game.add_player(player2)
    assert len(game.get_players_list()) == 2
    assert player2 in game.get_players_list()


def test_set_coords_to_player() -> None:
    game = Game()
    game.set_players_num(4)
    game.set_local_players_num(2)
    player = LocalPlayer("Test Player", "R")
    game.add_player(player)
    coords_list = [(0, 12), (1, 11)]
    game.set_coords_to_player(coords_list, player)
    assert len(game.board.list_player_marbles(player)) == 2
    assert game.board.list_player_marbles(player) == coords_list
    assert game.board.visual_board[0][12] == "R"
    assert game.board.visual_board[1][11] == "R"


def test_set_corner_to_player() -> None:
    game = Game()
    game.set_players_num(4)
    game.set_local_players_num(2)
    player1 = LocalPlayer("Test Player", "R")
    game.add_player(player1)
    game.set_corner_to_player(1, player1)
    assert len(game.board.list_player_marbles(player1)) == 10
    assert game.board.list_player_marbles(player1) == CORNER_1


def test_is_name_taken() -> None:
    game = Game()
    game.set_players_num(4)
    game.set_local_players_num(2)
    player = LocalPlayer("Test Player", "R")
    game.add_player(player)
    assert not game.is_name_taken("Name")
    assert game.is_name_taken("Test Player")


def test_is_color_taken() -> None:
    game = Game()
    game.set_players_num(4)
    game.set_local_players_num(2)
    player = LocalPlayer("Test Player", "R")
    game.add_player(player)
    assert game.is_color_taken("R")
    assert not game.is_color_taken("B")
    assert not game.is_color_taken("l")
    assert not game.is_color_taken("KKKK")


def test_new_local_player(monkeypatch) -> None:
    game = Game()
    game.set_players_num(4)
    game.set_local_players_num(2)
    inputs = iter(["John", "R"])  # Simulate user inputs for name and color
    def mock_input(prompt):
        return next(inputs)
    monkeypatch.setattr('builtins.input', mock_input)
    game.new_local_player()
    assert game.get_players_list()[-1].get_name() == "John"
    assert game.get_players_list()[-1].get_color() == "R"
    assert len(game.get_players_list()) == 1
    assert isinstance(game.get_players_list()[-1], LocalPlayer)
    inputs = iter(["l:d", "john", "peter", "R", "B"])  # Simulate user inputs for name and color
    def mock_input(prompt):
        return next(inputs)
    monkeypatch.setattr('builtins.input', mock_input)
    game.new_local_player()
    inputs = iter(["Amy", "F", "c"])  # Simulate user inputs for name and color
    def mock_input(prompt):
        return next(inputs)
    monkeypatch.setattr('builtins.input', mock_input)
    game.new_local_player()
    inputs = iter(["aaaaaaaasdasdfrewsdazxcbgytrfd", "kim", "y"])  # Simulate user inputs for name and color
    def mock_input(prompt):
        return next(inputs)
    monkeypatch.setattr('builtins.input', mock_input)
    game.new_local_player()


def test_new_comp_player() -> None:
    game = Game()
    game.set_players_num(4)
    game.set_local_players_num(2)
    game.new_comp_player()
    assert len(game.get_players_list()) == 1
    assert game.get_players_list()[-1].get_name() in ["Leonardo", "Raphael", "Michelangelo", "Donatello", "Shredder"]
    assert game.get_players_list()[-1].get_color() in ["P", "G", "C", "B", "Y", "R"]
    assert isinstance(game.get_players_list()[-1], ComputerPlayer)


def test_add_all_players(monkeypatch) -> None:
    game = Game()
    game.set_players_num(2)
    game.set_local_players_num(1)
    inputs = iter(["John", "R"])  # Simulate user inputs for name and color
    def mock_input(prompt):
        return next(inputs)
    monkeypatch.setattr('builtins.input', mock_input)
    game.add_all_players()
    assert len(game.get_players_list()) == 2
    assert isinstance(game.get_players_list()[1], ComputerPlayer)
    assert isinstance(game.get_players_list()[0], LocalPlayer)


def test_set_board_for_2() -> None:
    game = Game()
    game.set_players_num(2)
    game.set_local_players_num(1)
    player1 = LocalPlayer("Player1", "R")
    player2 = ComputerPlayer("Player2", "B")
    game.add_player(player1)
    game.add_player(player2)
    game.set_board_for_2([player1, player2])
    for coord in CORNER_1:
        assert game.board.game_board[coord] != 0
        assert coord in game.board.list_player_marbles(player1)
    for coord in CORNER_4:
        assert game.board.game_board[coord] != 0
        assert coord in game.board.list_player_marbles(player2)
    assert len(game.board.list_player_marbles(player1)) == 10
    assert len(game.board.list_player_marbles(player2)) == 10


def test_set_board_for_3() -> None:
    game = Game()
    game.set_players_num(3)
    game.set_local_players_num(1)
    player1 = LocalPlayer("Player1", "R")
    player2 = ComputerPlayer("Player2", "B")
    player3 = ComputerPlayer("Player3", "P")
    game.add_player(player1)
    game.add_player(player2)
    game.add_player(player3)
    game.set_board_for_3([player1, player2, player3])
    for coord in CORNER_2:
        assert game.board.game_board[coord] != 0
        assert coord in game.board.list_player_marbles(player1)
    for coord in CORNER_4:
        assert game.board.game_board[coord] != 0
        assert coord in game.board.list_player_marbles(player2)
    for coord in CORNER_6:
        assert game.board.game_board[coord] != 0
        assert coord in game.board.list_player_marbles(player3)
    assert len(game.board.list_player_marbles(player1)) == 10
    assert len(game.board.list_player_marbles(player2)) == 10
    assert len(game.board.list_player_marbles(player3)) == 10


def test_set_board_for_4() -> None:
    game = Game()
    game.set_players_num(4)
    game.set_local_players_num(1)
    player1 = LocalPlayer("Player1", "R")
    player2 = ComputerPlayer("Player2", "B")
    player3 = ComputerPlayer("Player3", "P")
    player4 = ComputerPlayer("Player4", "G")
    game.add_player(player1)
    game.add_player(player2)
    game.add_player(player3)
    game.add_player(player4)
    game.set_board_for_4([player1, player2, player3, player4])
    for coord in CORNER_2:
        assert game.board.game_board[coord] != 0
        assert coord in game.board.list_player_marbles(player1)
    for coord in CORNER_3:
        assert game.board.game_board[coord] != 0
        assert coord in game.board.list_player_marbles(player2)
    for coord in CORNER_5:
        assert game.board.game_board[coord] != 0
        assert coord in game.board.list_player_marbles(player3)
    for coord in CORNER_6:
        assert game.board.game_board[coord] != 0
        assert coord in game.board.list_player_marbles(player4)
    assert len(game.board.list_player_marbles(player1)) == 10
    assert len(game.board.list_player_marbles(player2)) == 10
    assert len(game.board.list_player_marbles(player3)) == 10
    assert len(game.board.list_player_marbles(player4)) == 10


def test_set_board_for_6() -> None:
    game = Game()
    game.set_players_num(6)
    game.set_local_players_num(2)
    player1 = LocalPlayer("Player1", "R")
    player2 = ComputerPlayer("Player2", "B")
    player3 = ComputerPlayer("Player3", "P")
    player4 = ComputerPlayer("Player4", "G")
    player5 = LocalPlayer("Player5", "C")
    player6 = ComputerPlayer("Player6", "Y")
    game.add_player(player1)
    game.add_player(player2)
    game.add_player(player3)
    game.add_player(player4)
    game.add_player(player5)
    game.add_player(player6)
    game.set_board_for_6([player1, player2, player3, player4, player5, player6])
    for coord in CORNER_1:
        assert game.board.game_board[coord] != 0
        assert coord in game.board.list_player_marbles(player1)
    for coord in CORNER_2:
        assert game.board.game_board[coord] != 0
        assert coord in game.board.list_player_marbles(player2)
    for coord in CORNER_3:
        assert game.board.game_board[coord] != 0
        assert coord in game.board.list_player_marbles(player3)
    for coord in CORNER_4:
        assert game.board.game_board[coord] != 0
        assert coord in game.board.list_player_marbles(player4)
    for coord in CORNER_5:
        assert game.board.game_board[coord] != 0
        assert coord in game.board.list_player_marbles(player5)
    for coord in CORNER_6:
        assert game.board.game_board[coord] != 0
        assert coord in game.board.list_player_marbles(player6)
    assert len(game.board.list_player_marbles(player1)) == 10
    assert len(game.board.list_player_marbles(player2)) == 10
    assert len(game.board.list_player_marbles(player3)) == 10
    assert len(game.board.list_player_marbles(player4)) == 10
    assert len(game.board.list_player_marbles(player5)) == 10
    assert len(game.board.list_player_marbles(player6)) == 10


def test_set_board() -> None:
    player1 = LocalPlayer("Player1", "R")
    player2 = LocalPlayer("Player2", "B")
    player3 = LocalPlayer("Player3", "P")
    player4 = LocalPlayer("Player4", "G")
    player5 = LocalPlayer("Player5", "C")
    player6 = ComputerPlayer("Player6", "Y")
    game1 = Game()
    game1.set_players_num(6)
    game1.set_local_players_num(5)
    game1.add_player(player1)
    game1.add_player(player2)
    game1.set_board(2)
    for coord in CORNER_1:
        assert game1.board.game_board[coord] != 0
        assert coord in game1.board.list_player_marbles(player1)
    for coord in CORNER_4:
        assert game1.board.game_board[coord] != 0
        assert coord in game1.board.list_player_marbles(player2)
    assert len(game1.board.list_player_marbles(player1)) == 10
    assert len(game1.board.list_player_marbles(player2)) == 10
    game2 = Game()
    game2.set_players_num(3)
    game2.set_local_players_num(3)
    game2.add_player(player1)
    game2.add_player(player2)
    game2.add_player(player3)
    game2.set_board(3)
    for coord in CORNER_2:
        assert game2.board.game_board[coord] != 0
        assert coord in game2.board.list_player_marbles(player1)
    for coord in CORNER_4:
        assert game2.board.game_board[coord] != 0
        assert coord in game2.board.list_player_marbles(player2)
    for coord in CORNER_6:
        assert game2.board.game_board[coord] != 0
        assert coord in game2.board.list_player_marbles(player3)
    game3 = Game()
    game3.set_players_num(4)
    game3.set_local_players_num(4)
    game3.add_player(player1)
    game3.add_player(player2)
    game3.add_player(player3)
    game3.add_player(player4)
    game3.set_board(4)
    for coord in CORNER_2:
        assert game3.board.game_board[coord] != 0
        assert coord in game3.board.list_player_marbles(player1)
    for coord in CORNER_3:
        assert game3.board.game_board[coord] != 0
        assert coord in game3.board.list_player_marbles(player2)
    for coord in CORNER_5:
        assert game3.board.game_board[coord] != 0
        assert coord in game3.board.list_player_marbles(player3)
    for coord in CORNER_6:
        assert game3.board.game_board[coord] != 0
        assert coord in game3.board.list_player_marbles(player4)
    game4 = Game()
    game4.set_players_num(6)
    game4.set_local_players_num(5)
    game4.add_player(player1)
    game4.add_player(player2)
    game4.add_player(player3)
    game4.add_player(player4)
    game4.add_player(player5)
    game4.add_player(player6)
    game4.set_board(6)
    for coord in CORNER_1:
        assert game4.board.game_board[coord] != 0
        assert coord in game4.board.list_player_marbles(player1)
    for coord in CORNER_2:
        assert game4.board.game_board[coord] != 0
        assert coord in game4.board.list_player_marbles(player2)
    for coord in CORNER_3:
        assert game4.board.game_board[coord] != 0
        assert coord in game4.board.list_player_marbles(player3)
    for coord in CORNER_4:
        assert game4.board.game_board[coord] != 0
        assert coord in game4.board.list_player_marbles(player4)
    for coord in CORNER_5:
        assert game4.board.game_board[coord] != 0
        assert coord in game4.board.list_player_marbles(player5)
    for coord in CORNER_6:
        assert game4.board.game_board[coord] != 0
        assert coord in game4.board.list_player_marbles(player6)


def test_new_game_settings(monkeypatch) -> None:
    game = Game()
    inputs = iter(["2", "1", "john", "R"])
    def mock_input(prompt):
        return next(inputs)
    monkeypatch.setattr('builtins.input', mock_input)
    game.new_game_settings()
    assert game.get_players_num() == 2
    assert game.get_local_players_num() == 1
    assert len(game.get_players_list()) == 2
    for player in game.get_players_list():
        assert len(game.board.list_player_marbles(player)) == 10
        assert isinstance(player, (LocalPlayer, ComputerPlayer))
    assert os.path.exists(game.get_log().get_log_path())
