import helper
from game import Game
from local_player import LocalPlayer
from computer_player import ComputerPlayer
from marble import Marble
import os
import datetime


def test_insert_players() -> None:
    game = Game()
    players_info = [["player1", "R", "1", "1", "0", "local"], ["player2", "B", "4", "0", "1", "computer"]]
    game.insert_players(players_info)
    assert len(game.get_players_list()) == 2
    assert game.get_players_num() == 2
    assert game.get_local_players_num() == 1
    for player in game.get_players_list():
        if player.get_name() == "player1":
            assert player.get_color() == "R"
            assert player.get_corner_num() == 1
            assert player.get_wins() == 1
            assert player.get_losses() == 0
            assert isinstance(player, LocalPlayer)
        else:
            assert player.get_color() == "B"
            assert player.get_corner_num() == 4
            assert player.get_wins() == 0
            assert player.get_losses() == 1
            assert isinstance(player, ComputerPlayer)


def test_insert_marbles() -> None:
    game = Game()
    assert game.board.game_board[(0, 12)] == 0
    assert game.board.game_board[(1, 11)] == 0
    marbles_info = [["R", (0, 12), 1], ["B", (1, 11), 2]]
    game.insert_marbles(marbles_info)
    assert isinstance(game.board.game_board[(0, 12)], Marble)
    assert game.board.game_board[(0, 12)].get_color() == "R"
    assert game.board.game_board[(1, 11)].get_color() == "B"
    assert game.board.game_board[(0, 12)].get_number() == 1
    assert game.board.game_board[(1, 11)].get_number() == 2
    assert isinstance(game.board.game_board[(1, 11)], Marble)


def test_did_complete_round() -> None:
    game = Game()
    player1 = LocalPlayer("player1", "R")
    player2 = LocalPlayer("player2", "B")
    game.add_player(player1)
    game.add_player(player2)
    game.get_log().add_to_log("PLAYER: player1 (R) ")
    assert helper.last_played(game.get_log().get_log_path()) == "player1"
    assert not game.did_complete_round()
    game.get_log().add_to_log("PLAYER: player2 (B) ")
    assert helper.last_played(game.get_log().get_log_path()) == "player2"
    assert game.did_complete_round()
    os.remove(game.get_log().get_log_path())


def test_half_round(monkeypatch) -> None:
    game = Game()
    player1 = LocalPlayer("player1", "R")
    player2 = LocalPlayer("player2", "B")
    game.add_player(player1)
    game.add_player(player2)
    game.set_board(2)
    game.get_log().add_to_log("PLAYER: player1 (R) ")
    assert not game.did_complete_round()
    assert helper.last_played(game.get_log().get_log_path()) == "player1"
    inputs = iter(["0", "ul"])  # Simulate user inputs for name and color
    def mock_input(prompt):
        return next(inputs)
    monkeypatch.setattr('builtins.input', mock_input)
    game.half_round()
    assert game.did_complete_round()
    assert helper.last_played(game.get_log().get_log_path()) == "player2"
    os.remove(game.get_log().get_log_path())


def test_older_game_settings(monkeypatch) -> None:
    game1 = Game()
    inputs = iter(["2", "2", "john", "R", "peter", "B"])
    def mock_input(prompt):
        return next(inputs)
    monkeypatch.setattr('builtins.input', mock_input)
    game1.new_game_settings()
    game1_name = game1.get_log().get_log_name()
    game1_path = game1.get_log().get_log_path()
    game2 = Game()
    inputs = iter([game1_name[5:-4], "y"])
    def mock_input(prompt):
        return next(inputs)
    monkeypatch.setattr('builtins.input', mock_input)
    game_choice = helper.choose_game()
    game2.older_game_settings(game_choice)
    assert len(game2.get_players_list()) == 2
    assert game2.get_players_num() == 2
    assert game2.get_local_players_num() == 2
    assert game2.get_players_list()[0].get_name() == "john"
    assert game2.get_players_list()[0].get_color() == "R"
    assert game2.get_players_list()[1].get_name() == "peter"
    assert game2.get_players_list()[1].get_color() == "B"
    for coord in helper.CORNER_1:
        assert not game2.board.is_coord_empty(coord)
    for coord in helper.CORNER_4:
        assert not game2.board.is_coord_empty(coord)
    os.remove(game1_path)


helper.logs_folder()      # opens this file for the tests if it doesn't already exist


def test_get_player_info() -> None:
    game = Game()
    game.set_players_num(2)
    game.set_local_players_num(1)
    player1 = LocalPlayer("player1", "R", 1, 2, 3)
    player2 = ComputerPlayer("player2", "B", 4, 5, 6)
    game.add_player(player1)
    game.add_player(player2)
    expected_str = "Name: player1, Color: R, Corner: 1, Wins: 2, Losses: 3, Type: local" + "\n"
    expected_str += "Name: player2, Color: B, Corner: 4, Wins: 5, Losses: 6, Type: computer" + "\n"
    assert game.get_player_info() == expected_str


def test_start_info() -> None:
    game = Game()
    game.set_players_num(2)
    game.set_local_players_num(2)
    expected_start_info = "\n####################### GAME LOG #######################\n"
    cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expected_start_info += "GAME START: " + cur_time + "\n"
    expected_start_info += "PLAYERS INFO:" + "\n" + game.get_player_info()
    assert game.start_info() == expected_start_info


def test_create_log_file() -> None:
    game = Game()
    game.set_players_num(2)
    game.set_local_players_num(1)
    game.create_log_file()
    log_path = game.get_log().get_log_path()
    assert os.path.exists(log_path)
    os.remove(log_path)


def test_continue_game_choice(monkeypatch) -> None:
    game = Game()
    game.set_players_num(2)
    game.set_local_players_num(2)
    monkeypatch.setattr('builtins.input', lambda _: "y")  # Mocking user input
    assert game.continue_game_choice()
    monkeypatch.setattr('builtins.input', lambda _: "n")  # Mocking user input
    assert not game.continue_game_choice()
