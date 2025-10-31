from local_player import LocalPlayer


def test_local_player_init() -> None:
    player1 = LocalPlayer("Alice", "red")
    assert player1.get_name() == "Alice"
    assert player1.get_color() == "red"
    assert player1.get_corner_num() == 0
    assert player1.get_wins() == 0
    assert player1.get_losses() == 0
    assert isinstance(player1, LocalPlayer)
    player2 = LocalPlayer("Bob", "lilac", 2, 3, 9)
    assert player2.get_name() == "Bob"
    assert player2.get_color() == "lilac"
    assert isinstance(player2, LocalPlayer)
    assert player2.get_corner_num() == 2
    assert player2.get_wins() == 3
    assert player2.get_losses() == 9


def test_set_wins_losses() -> None:
    player1 = LocalPlayer("Bob", "blue")
    player1.set_wins(5)
    player1.set_losses(3)
    assert player1.get_wins() == 5
    assert player1.get_losses() == 3
    player2 = LocalPlayer("KIM", "brown", 3, 2, 7)
    player2.set_wins(8)
    player2.set_losses(4)
    assert player2.get_wins() == 8
    assert player2.get_losses() == 4


def test_add_win_loss() -> None:
    player1 = LocalPlayer("Charlie", "green")
    player1.add_win()
    player1.add_loss()
    assert player1.get_wins() == 1
    assert player1.get_losses() == 1
    player2 = LocalPlayer("Addison", "ray", wins=2, losses=3)
    player2.add_win()
    player2.add_loss()
    assert player2.get_wins() == 3
    assert player2.get_losses() == 4
    player3 = LocalPlayer("Marlyn", "BLACK", wins=-1, losses=-1)
    player3.add_win()
    player3.add_loss()
    assert player3.get_wins() == 0
    assert player3.get_losses() == 0


def test_choose_marble(monkeypatch) -> None:
    player1 = LocalPlayer("Dave", "yellow")
    # Mocking user input
    monkeypatch.setattr('builtins.input', lambda _: "0")
    assert player1.choose_marble() == 0
    monkeypatch.setattr('builtins.input', lambda _: "1")
    assert player1.choose_marble() == 1
    monkeypatch.setattr('builtins.input', lambda _: "invalid_input")
    monkeypatch.setattr('builtins.input', lambda _: "9")
    assert player1.choose_marble() == 9
    monkeypatch.setattr('builtins.input', lambda _: "-1")
    assert player1.choose_marble() == -1


def test_choose_direction(monkeypatch) -> None:
    player = LocalPlayer("Eve", "purple")
    # Mocking user input
    monkeypatch.setattr('builtins.input', lambda _: "ul")
    assert player.choose_direction() == "ul"
    monkeypatch.setattr('builtins.input', lambda _: "ur")
    assert player.choose_direction() == "ur"
    monkeypatch.setattr('builtins.input', lambda _: "dl")
    assert player.choose_direction() == "dl"
    monkeypatch.setattr('builtins.input', lambda _: "invalid_input")
    monkeypatch.setattr('builtins.input', lambda _: "dr")
    assert player.choose_direction() == "dr"
    monkeypatch.setattr('builtins.input', lambda _: "jl")
    assert player.choose_direction() == "jl"
    monkeypatch.setattr('builtins.input', lambda _: "jr")
    assert player.choose_direction() == "jr"


def test_set_corner_num() -> None:
    player1 = LocalPlayer("Frank", "orange")
    player1.set_corner_num(2)
    assert player1.get_corner_num() == 2
    player2 = LocalPlayer("georgia", "peaches", 4)
    player2.set_corner_num(2)
    assert player2.get_corner_num() == 2
    player3 = LocalPlayer("Kelly", "PINK", -1)
    player3.set_corner_num(220)
    assert player3.get_corner_num() == 220


# Test for getting name, color, wins, losses, corner num
def test_getters() -> None:
    player1 = LocalPlayer("George", "cyan", 3, 10, 5)
    assert player1.get_name() == "George"
    assert player1.get_color() == "cyan"
    assert player1.get_wins() == 10
    assert player1.get_losses() == 5
    assert player1.get_corner_num() == 3
    player2 = LocalPlayer("queen of england", "yellow", 0.5, -1, 300)
    assert player2.get_name() == "queen of england"
    assert player2.get_color() == "yellow"
    assert player2.get_corner_num() == 0.5
    assert player2.get_wins() == -1
    assert player2.get_losses() == 300
    player3 = LocalPlayer("prince harry", "color")
    assert player3.get_name() == "prince harry"
    assert player3.get_color() == "color"
    assert player3.get_corner_num() == 0
    assert player3.get_wins() == 0
    assert player3.get_losses() == 0
