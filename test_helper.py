from helper import *
from colorama import Fore
import os
from unittest.mock import patch


def test_create_board_list() -> None:
    board = create_board_list()
    assert len(board) == 17  # Check if the board has 17 rows
    # Check if each row has 25 columns
    for row in board:
        assert len(row) == 25
    expected = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    assert board == expected


def test_create_board_dict() -> None:
    board_list = create_board_list()
    board_dict = create_board_dict(board_list)
    expected_board_dict = {(0, 12): 0, (1, 11): 0, (1, 13): 0, (2, 10): 0, (2, 12): 0, (2, 14): 0, (3, 9): 0,
                           (3, 11): 0, (3, 13): 0,
                           (3, 15): 0, (4, 0): 0, (4, 2): 0, (4, 4): 0, (4, 6): 0, (4, 8): 0, (4, 10): 0, (4, 12): 0,
                           (4, 14): 0, (4, 16): 0,
                           (4, 18): 0, (4, 20): 0, (4, 22): 0, (4, 24): 0, (5, 1): 0, (5, 3): 0, (5, 5): 0, (5, 7): 0,
                           (5, 9): 0, (5, 11): 0,
                           (5, 13): 0, (5, 15): 0, (5, 17): 0, (5, 19): 0, (5, 21): 0, (5, 23): 0, (6, 2): 0, (6, 4): 0,
                           (6, 6): 0, (6, 8): 0,
                           (6, 10): 0, (6, 12): 0, (6, 14): 0, (6, 16): 0, (6, 18): 0, (6, 20): 0, (6, 22): 0,
                           (7, 3): 0, (7, 5): 0,
                           (7, 7): 0, (7, 9): 0, (7, 11): 0, (7, 13): 0, (7, 15): 0, (7, 17): 0, (7, 19): 0, (7, 21): 0,
                           (8, 4): 0, (8, 6): 0,
                           (8, 8): 0, (8, 10): 0, (8, 12): 0, (8, 14): 0, (8, 16): 0, (8, 18): 0, (8, 20): 0, (9, 3): 0,
                           (9, 5): 0, (9, 7): 0,
                           (9, 9): 0, (9, 11): 0, (9, 13): 0, (9, 15): 0, (9, 17): 0, (9, 19): 0, (9, 21): 0,
                           (10, 2): 0, (10, 4): 0,
                           (10, 6): 0, (10, 8): 0, (10, 10): 0, (10, 12): 0, (10, 14): 0, (10, 16): 0, (10, 18): 0,
                           (10, 20): 0, (10, 22): 0,
                           (11, 1): 0, (11, 3): 0, (11, 5): 0, (11, 7): 0, (11, 9): 0, (11, 11): 0, (11, 13): 0,
                           (11, 15): 0, (11, 17): 0,
                           (11, 19): 0, (11, 21): 0, (11, 23): 0, (12, 0): 0, (12, 2): 0, (12, 4): 0, (12, 6): 0,
                           (12, 8): 0, (12, 10): 0,
                           (12, 12): 0, (12, 14): 0, (12, 16): 0, (12, 18): 0, (12, 20): 0, (12, 22): 0, (12, 24): 0,
                           (13, 9): 0, (13, 11): 0,
                           (13, 13): 0, (13, 15): 0, (14, 10): 0, (14, 12): 0, (14, 14): 0, (15, 11): 0, (15, 13): 0,
                           (16, 12): 0}
    assert board_dict == expected_board_dict


def test_string_to_color() -> None:
    assert string_to_color("B") == Fore.BLUE
    assert string_to_color("C") == Fore.CYAN
    assert string_to_color("G") == Fore.GREEN
    assert string_to_color("P") == Fore.MAGENTA
    assert string_to_color("R") == Fore.RED
    assert string_to_color("Y") == Fore.YELLOW


def test_logs_folder(tmp_path) -> None:
    assert not os.path.exists(os.path.join(tmp_path, 'logs'))
    logs_folder()
    assert os.path.exists(os.path.join('logs'))


def test_naming_game() -> None:
    new_name = naming_game()
    directory = os.fsencode("logs")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        assert filename != new_name


def test_load_older_option(monkeypatch) -> None:
    monkeypatch.setattr('builtins.input', lambda _: "new")
    assert not load_older_option()
    monkeypatch.setattr('builtins.input', lambda _: "old")
    assert load_older_option()
    inputs = iter(["W", "new"])

    def mock_input(prompt):
        return next(inputs)

    monkeypatch.setattr('builtins.input', mock_input)
    assert not load_older_option()


def test_choose_game(monkeypatch) -> None:
    path1 = os.path.join(os.getcwd(), "logs", "game_" + "tester1" + ".txt")
    with open(path1, "w") as file:
        file.write("tester1")
    inputs = iter(["W", "tester1"])

    def mock_input(prompt):
        return next(inputs)

    monkeypatch.setattr('builtins.input', mock_input)
    game_choice = choose_game()
    assert game_choice[0] == path1
    assert game_choice[1] == "game_tester1.txt"
    path2 = os.path.join(os.getcwd(), "logs", "game_" + "tester2" + ".txt")
    with open(path2, "w") as file:
        file.write("WINNER:")
    inputs = iter(["tester2", "tester1"])

    def mock_input(prompt):
        return next(inputs)

    monkeypatch.setattr('builtins.input', mock_input)
    game_choice = choose_game()
    assert game_choice[0] == path1
    assert game_choice[1] == "game_tester1.txt"
    os.remove(path1)
    os.remove(path2)


def test_choose_game_to_read(monkeypatch) -> None:
    path1 = os.path.join(os.getcwd(), "logs", "game_" + "tester1" + ".txt")
    with open(path1, "w") as file:
        file.write("tester1")
    inputs = iter(["W", "tester1"])

    def mock_input(prompt):
        return next(inputs)

    monkeypatch.setattr('builtins.input', mock_input)
    game_choice = choose_game_to_read()
    assert game_choice[0] == path1
    assert game_choice[1] == "game_tester1.txt"
    os.remove(path1)


def test_did_game_over() -> None:
    path1 = os.path.join(os.getcwd(), "logs", "game_" + "tester1" + ".txt")
    with open(path1, "w") as file:
        file.write("tester1")
    path2 = os.path.join(os.getcwd(), "logs", "game_" + "tester2" + ".txt")
    with open(path2, "w") as file:
        file.write("WINNER:")
    assert not did_game_over(path1)
    assert did_game_over(path2)
    os.remove(path1)
    os.remove(path2)


def test_resume_option(monkeypatch) -> None:
    monkeypatch.setattr('builtins.input', lambda _: "n")
    assert not resume_option()
    monkeypatch.setattr('builtins.input', lambda _: "y")
    assert resume_option()
    inputs = iter(["kal", "n"])

    def mock_input(prompt):
        return next(inputs)

    monkeypatch.setattr('builtins.input', mock_input)
    assert not resume_option()


def test_collect_players_info() -> None:
    info = "PLAYERS INFO:\n" + \
           "Name: kim, Color: P, Corner: 1, Wins: 0, Losses: 0, Type: local\n" + \
           "Name: Leonardo, Color: G, Corner: 4, Wins: 0, Losses: 0, Type: computer\n"
    path1 = os.path.join(os.getcwd(), "logs", "game_" + "tester1" + ".txt")
    with open(path1, "w") as file:
        file.write(info)
    result = collect_players_info(path1)
    player1 = ["kim", "P", "1", "0", "0", "local"]
    player2 = ["Leonardo", "G", "4", "0", "0", "computer"]
    assert result == [player1, player2]
    os.remove(path1)


def test_is_there_board() -> None:
    path1 = os.path.join(os.getcwd(), "logs", "game_" + "tester1" + ".txt")
    with open(path1, "w") as file:
        file.write("tester1")
    assert not is_there_board(path1)
    with open(path1, "a") as file:
        file.write("State of the board:")
    assert is_there_board(path1)
    os.remove(path1)


def test_collect_marbles_info() -> None:
    path1 = os.path.join(os.getcwd(), "logs", "game_" + "tester1" + ".txt")
    with open(path1, "w") as file:
        file.write("Marbles state: \n" + "[R : (0, 12) : 4], [B : (1, 11) : 5], \n")
    result = collect_marbles_info(path1)
    marble1 = ["R", (0, 12), 4]
    marble2 = ["B", (1, 11), 5]
    assert marble1 in result
    assert marble2 in result
    os.remove(path1)


def test_last_played() -> None:
    path1 = os.path.join(os.getcwd(), "logs", "game_" + "tester1" + ".txt")
    with open(path1, "w") as file:
        file.write("PLAYER: kim (P) \n")
    assert last_played(path1) == "kim"
    os.remove(path1)


def test_read_any_log(capsys) -> None:
    path1 = os.path.join(os.getcwd(), "logs", "game_" + "tester1" + ".txt")
    with open(path1, "w") as file:
        file.write("tester")
    expected_output = "tester\n################### END OF GAME LOG ###################\n\n"
    read_any_log(path1)
    captured = capsys.readouterr()
    assert captured.out == expected_output
    os.remove(path1)


def test_choose_players_num(monkeypatch) -> None:
    monkeypatch.setattr('builtins.input', lambda _: "2")
    assert choose_players_num() == 2
    monkeypatch.setattr('builtins.input', lambda _: "3")
    assert choose_players_num() == 3
    monkeypatch.setattr('builtins.input', lambda _: "4")
    assert choose_players_num() == 4
    monkeypatch.setattr('builtins.input', lambda _: "6")
    assert choose_players_num() == 6
    with patch('builtins.input', side_effect=["5", "2"]):
        assert choose_players_num() == 2


def test_choose_local_players_num(monkeypatch) -> None:
    monkeypatch.setattr('builtins.input', lambda _: "1")
    assert choose_local_num(2) == 1
    monkeypatch.setattr('builtins.input', lambda _: "2")
    assert choose_local_num(2) == 2
    monkeypatch.setattr('builtins.input', lambda _: "3")
    assert choose_local_num(4) == 3
    monkeypatch.setattr('builtins.input', lambda _: "4")
    assert choose_local_num(6) == 4
    monkeypatch.setattr('builtins.input', lambda _: "5")
    assert choose_local_num(6) == 5
    monkeypatch.setattr('builtins.input', lambda _: "6")
    assert choose_local_num(6) == 6
    with patch('builtins.input', side_effect=["k", "2"]):
        assert choose_players_num() == 2


def test_get_sound_path() -> None:
    assert get_sound_path("tester") == os.path.join(os.getcwd(), "sounds", "tester.mp3")


def test_version_choice(monkeypatch) -> None:
    monkeypatch.setattr('builtins.input', lambda _: "r")
    assert version_choice()
    monkeypatch.setattr('builtins.input', lambda _: "c")
    assert not version_choice()
    inputs = iter(["invalid", "r"])

    def mock_input(prompt):
        return next(inputs)

    monkeypatch.setattr('builtins.input', mock_input)
    assert version_choice()


def test_print_help(capsys) -> None:
    print_help()
    captured = capsys.readouterr()
    assert "EXPLANATION" in captured.out
    assert "NEW GAME OPTION" in captured.out
    assert "OLDER GAME OPTION" in captured.out
    assert "RULES" in captured.out
    assert "CAPTURE" in captured.out
