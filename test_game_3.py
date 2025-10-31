from game import Game
from board import Board
from marble import Marble
from local_player import LocalPlayer
from computer_player import ComputerPlayer
from helper import *
import datetime


def test_hop_choice(monkeypatch) -> None:
    game = Game()
    game.set_players_num(2)
    game.set_local_players_num(2)
    monkeypatch.setattr('builtins.input', lambda _: "hop")
    assert game.hop_choice()
    monkeypatch.setattr('builtins.input', lambda _: "step")
    assert not game.hop_choice()


def test_another_hop_choice(monkeypatch) -> None:
    game = Game()
    game.set_players_num(2)
    game.set_local_players_num(2)
    monkeypatch.setattr('builtins.input', lambda _: "Y")
    assert game.another_hop_choice()
    monkeypatch.setattr('builtins.input', lambda _: "N")
    assert not game.another_hop_choice()


def test_local_one_hop(monkeypatch) -> None:
    game = Game()
    game.set_players_num(2)
    game.set_local_players_num(2)
    player = LocalPlayer("Ruth", "P")
    game.add_player(player)
    marble = Marble("R", (2, 12), 8)  # create a marble
    marble2 = Marble("R", (3, 11), 9)
    game.board.add_marble(marble)
    game.board.add_marble(marble2)
    monkeypatch.setattr('builtins.input', lambda _: "dl")
    game.local_one_hop(marble, player)
    assert game.board.game_board[(4, 10)] == marble
    assert game.board.game_board[(2, 12)] == 0
    assert game.board.game_board[(3, 11)] == marble2


def test_local_hop_move(monkeypatch) -> None:
    game = Game()
    game.set_players_num(2)
    game.set_local_players_num(2)
    player = LocalPlayer("Ruth", "P")
    game.add_player(player)
    marble = Marble("R", (2, 12), 8)  # create a marble
    marble2 = Marble("R", (3, 11), 9)
    game.board.add_marble(marble)
    game.board.add_marble(marble2)
    inputs = iter(["dl", "Y", "ur", "N"])
    def mock_input(prompt):
        return next(inputs)
    monkeypatch.setattr('builtins.input', mock_input)
    game.local_hop_move(marble, player)
    assert game.board.game_board[(4, 10)] == 0
    assert game.board.game_board[(2, 12)] == marble
    assert game.board.game_board[(3, 11)] == marble2


def test_local_step_move(monkeypatch) -> None:
    game = Game()
    game.set_players_num(2)
    game.set_local_players_num(2)
    player = LocalPlayer("Ruth", "P")
    game.add_player(player)
    marble = Marble("R", (2, 12), 8)
    game.board.add_marble(marble)
    inputs = iter(["jl"])
    def mock_input(prompt):
        return next(inputs)
    monkeypatch.setattr('builtins.input', mock_input)
    game.local_step_move(marble, player)
    assert game.board.game_board[(2, 10)] == marble
    assert game.board.game_board[(2, 12)] == 0


def test_comp_one_hop() -> None:
    game = Game()
    game.set_players_num(2)
    game.set_local_players_num(2)
    player = ComputerPlayer("Ruth", "P")
    game.add_player(player)
    marble1 = Marble("R", (0, 12), 8)
    marble2 = Marble("R", (1, 11), 9)
    marble3 = Marble("B", (1, 13), 7)
    marble4 = Marble("B", (2, 14), 6)
    game.board.add_marble(marble4)
    game.board.add_marble(marble3)
    game.board.add_marble(marble1)
    game.board.add_marble(marble2)
    assert game.board.game_board[(0, 12)] == marble1
    game.comp_one_hop(marble1)
    assert game.board.game_board[(0, 12)] == 0
    assert game.board.game_board[(2, 10)] == marble1


def test_comp_hop_move() -> None:
    game = Game()
    game.set_players_num(2)
    game.set_local_players_num(2)
    player = ComputerPlayer("Ruth", "P")
    game.add_player(player)
    marble1 = Marble("R", (0, 12), 8)
    marble2 = Marble("R", (1, 11), 9)
    marble3 = Marble("B", (1, 13), 7)
    marble4 = Marble("B", (2, 14), 6)
    game.board.add_marble(marble4)
    game.board.add_marble(marble3)
    game.board.add_marble(marble1)
    game.board.add_marble(marble2)
    assert game.board.game_board[(0, 12)] == marble1
    assert game.board.game_board[(2, 10)] == 0
    game.comp_hop_move(marble1, player)
    assert game.board.game_board[(0, 12)] == 0 or game.board.game_board[(2, 10)] == 0


def test_comp_step_move() -> None:
    game = Game()
    game.set_players_num(2)
    game.set_local_players_num(2)
    player = ComputerPlayer("Ruth", "P")
    game.add_player(player)
    marble1 = Marble("R", (0, 12), 8)
    marble2 = Marble("R", (1, 11), 9)
    game.board.add_marble(marble1)
    game.board.add_marble(marble2)
    assert game.board.game_board[(0, 12)] == marble1
    assert game.board.game_board[(1, 13)] == 0
    game.comp_step_move(marble1)
    assert game.board.game_board[(1, 13)] == marble1
    assert game.board.game_board[(0, 12)] == 0


def test_valid_marble_for_local(monkeypatch) -> None:
    game = Game()
    game.set_players_num(4)
    game.set_local_players_num(3)
    player = LocalPlayer("Ruth", "P")
    game.add_player(player)
    marble1 = Marble("P", (2, 12), 8)
    marble2 = Marble("R", (3, 11), 9)
    game.board.add_marble(marble1)
    game.board.add_marble(marble2)
    monkeypatch.setattr('builtins.input', lambda _: "8")
    marble = game.valid_marble_for_local(player)
    assert marble == marble1


def test_turn_of_local(monkeypatch) -> None:
    game1 = Game()
    game1.set_players_num(2)
    game1.set_local_players_num(2)
    player = LocalPlayer("Ruth", "R")
    game1.add_player(player)
    marble1 = Marble("R", (0, 12), 8)
    marble2 = Marble("R", (1, 13), 9)
    game1.board.add_marble(marble1)
    game1.board.add_marble(marble2)
    inputs = iter(["8", "step", "dl"])
    def mock_input(prompt):
        return next(inputs)
    monkeypatch.setattr('builtins.input', mock_input)
    assert game1.turn_of_local(player) == [(0, 12), (1, 11)]
    player2 = LocalPlayer("bader", "P")
    marble3 = Marble("P", (0, 12), 4)
    marble4 = Marble("R", (2, 10), 2)
    marble5 = Marble("R", (2, 12), 3)
    marble6 = Marble("R", (2, 14), 5)
    game1.board.add_marble(marble3)
    game1.board.add_marble(marble4)
    game1.board.add_marble(marble5)
    game1.board.add_marble(marble6)
    assert game1.turn_of_local(player2) == "stuck"


def test_valid_marble_for_comp() -> None:
    game = Game()
    game.set_players_num(2)
    game.set_local_players_num(2)
    player = ComputerPlayer("dylan", "R")
    game.add_player(player)
    i = 0
    for coord in CORNER_1:
        cur_marble = Marble("R", coord, i)
        game.board.add_marble(cur_marble)
        i += 1
    j = 0
    for coord in CORNER_2:
        cur_marble = Marble("P", coord, i)
        game.board.add_marble(cur_marble)
        j += 1
    marble = game.valid_marble_for_comp(player)
    assert isinstance(marble, Marble)  # Check if a marble object is returned
    # Check if the returned marble can actually move
    assert game.board.can_marble_move(marble)
    assert marble.get_color() == "R"
    assert marble.get_location() in CORNER_1


def test_turn_of_comp() -> None:
    game1 = Game()
    game1.set_players_num(2)
    game1.set_local_players_num(2)
    player1 = ComputerPlayer("dylan", "R")
    game1.add_player(player1)
    turn_result = game1.turn_of_comp(player1)
    assert turn_result == "stuck"
    board2 = Board()
    game2 = Game()
    game2.set_players_num(2)
    game2.set_local_players_num(1)
    player2 = ComputerPlayer("dyl", "P")
    game2.add_player(player2)
    marble1 = Marble("P", (0, 12), 4)
    game2.board.add_marble(marble1)
    turn_result = game2.turn_of_comp(player2)
    assert turn_result in [[(0, 12), (1, 11)], [(0, 12), (1, 13)]]
    # TODO - OPTIONAL EXTENT


def test_turn_details() -> None:
    game1 = Game()
    game1.set_players_num(2)
    game1.set_local_players_num(1)
    player1 = ComputerPlayer("dylan", "R")
    game1.add_player(player1)
    details = game1.turn_details(player1, "stuck")
    expected = "PLAYER: dylan (R) \n"
    expected += "TIME: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    expected += "MOVE: Player couldn't make a any moves.\n"
    expected += "State of the board:" + "\n"
    assert expected in details
    marble1 = Marble("R", (0, 12), 7)
    game1.board.add_marble(marble1)
    details = game1.turn_details(player1, [(0, 12), (1, 11)])
    expected = "PLAYER: dylan (R) \n"
    expected += "TIME: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    expected += "MOVE: Player moved marble in location (0, 12) to (1, 11).\n"
    expected += "State of the board:" + "\n"
    assert expected in details


def test_marbles_details() -> None:
    pass
    game1 = Game()
    marble1 = Marble("R", (0, 12), 8)
    marble2 = Marble("R", (1, 13), 9)
    marble3 = Marble("P", (0, 12), 4)
    marble4 = Marble("R", (2, 10), 2)
    marble5 = Marble("R", (2, 12), 3)
    marble6 = Marble("R", (2, 14), 5)
    game1.board.add_marble(marble1)
    game1.board.add_marble(marble2)
    game1.board.add_marble(marble3)
    game1.board.add_marble(marble4)
    game1.board.add_marble(marble5)
    game1.board.add_marble(marble6)
    expected = "[R : (0, 12) : 8], [R : (1, 13) : 9], [R : (2, 10) : 2], [R : (2, 12) : 3], [R : (2, 14) : 5],"
    assert expected in game1.marbles_details()


def test_end_details() -> None:
    game1 = Game()
    game1.set_players_num(2)
    game1.set_local_players_num(1)
    player1 = ComputerPlayer("dylan", "R", 1)
    game1.add_player(player1)
    game1.set_coords_to_player(CORNER_4, player1)
    details = game1.end_details(player1)
    expected = "dylan has reached the opposite corner and won the game! \n"
    assert expected in details


def test_declare_winner(capsys) -> None:
    game1 = Game()
    game1.set_players_num(2)
    game1.set_local_players_num(1)
    player1 = ComputerPlayer("dylan", "R")
    game1.add_player(player1)
    game1.declare_winner(player1)
    captured = capsys.readouterr()
    assert f"{player1.get_name()} WINS THE GAME!!!" in captured.out
    assert game1.declare_winner(player1) == player1


def test_update_wins_losses() -> None:
    game1 = Game()
    game1.set_players_num(2)
    game1.set_local_players_num(1)
    player1 = ComputerPlayer("dylan", "R")
    player2 = ComputerPlayer("yoshi", "P")
    game1.add_player(player1)
    game1.add_player(player2)
    game1.update_wins_losses(player1)
    assert player1.get_wins() == 1
    assert player1.get_losses() == 0
    assert player2.get_wins() == 0
    assert player2.get_losses() == 1


def test_another_game(monkeypatch) -> None:
    game1 = Game()
    game1.set_players_num(2)
    game1.set_local_players_num(1)
    monkeypatch.setattr('builtins.input', lambda _: "yes")
    assert game1.another_game()
    monkeypatch.setattr('builtins.input', lambda _: "no")
    assert not game1.another_game()


def test_reset_board_and_name() -> None:
    game1 = Game()
    game1.set_players_num(2)
    game1.set_local_players_num(1)
    game1.create_log_file()
    old_name = game1.get_log().get_log_name()
    old_board = game1.board
    game1.reset_board_and_name()
    assert old_name != game1.get_log().get_log_name()
    assert old_board != game1.board


def test_one_round_no_winner(monkeypatch, capsys) -> None:
    game1 = Game()
    game1.set_players_num(2)
    game1.set_local_players_num(1)
    player1 = LocalPlayer("dylan", "R")
    player2 = ComputerPlayer("yoshi", "B")
    game1.add_player(player1)
    game1.add_player(player2)
    game1.set_board(2)
    inputs = iter(["9", "dl"])
    def mock_input(prompt):
        return next(inputs)
    monkeypatch.setattr('builtins.input', mock_input)
    result = game1.one_round()
    # Check if no winner is declared
    captured = capsys.readouterr()
    assert "wins the game" not in captured.out
    assert result


def test_one_round_winner(monkeypatch, capsys) -> None:
    game1 = Game()
    game1.set_players_num(2)
    game1.set_local_players_num(1)
    player1 = LocalPlayer("dylan", "R", 1)
    player2 = ComputerPlayer("yoshi", "B", 4)
    game1.add_player(player1)
    game1.add_player(player2)
    game1.set_corner_to_player(4, player1)
    game1.set_corner_to_player(2, player2)
    inputs = iter(["0", "ul"])
    def mock_input(prompt):
        return next(inputs)
    monkeypatch.setattr('builtins.input', mock_input)
    result = game1.one_round()
    # Check if no winner is declared
    captured = capsys.readouterr()
    assert "wins the game" not in captured.out
    assert result
    inputs = iter(["0", "dr", "no"])
    def mock_input(prompt):
        return next(inputs)
    monkeypatch.setattr('builtins.input', mock_input)
    result = game1.one_round()
    captured = capsys.readouterr()
    assert f"{player1.get_name()} WINS THE GAME!!!" in captured.out
    assert player1.get_wins() == 1
    assert player1.get_losses() == 0
    assert player2.get_wins() == 0
    assert player2.get_losses() == 1
    assert not result

