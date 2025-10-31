from computer_player import ComputerPlayer


def test_computer_player_init() -> None:
    player1 = ComputerPlayer("Alice", "red")
    assert player1.get_name() == "Alice"
    assert player1.get_color() == "red"
    assert player1.get_corner_num() == 0
    assert player1.get_wins() == 0
    assert player1.get_losses() == 0
    assert isinstance(player1, ComputerPlayer)
    player2 = ComputerPlayer("Bob", "kiki", 2, 3, 4)
    assert player2.get_name() == "Bob"
    assert player2.get_color() == "kiki"
    assert isinstance(player2, ComputerPlayer)
    assert player2.get_corner_num() == 2
    assert player2.get_wins() == 3
    assert player2.get_losses() == 4


# Test for getting name, color, wins, losses, corner num
def test_getters() -> None:
    player1 = ComputerPlayer("KEREN", "peles", -1, 5, 7)
    assert player1.get_name() == "KEREN"
    assert player1.get_color() == "peles"
    assert player1.get_corner_num() == -1
    assert player1.get_wins() == 5
    assert player1.get_losses() == 7
    player2 = ComputerPlayer("drake", "josh", 90, 0, 2)
    assert player2.get_name() == "drake"
    assert player2.get_color() == "josh"
    assert player2.get_corner_num() == 90
    assert player2.get_wins() == 0
    assert player2.get_losses() == 2
    player3 = ComputerPlayer("jackson", "cyan", 33.5, -5, 1)
    assert player3.get_corner_num() == 33.5
    assert player3.get_wins() == -5
    assert player3.get_losses() == 1


# Test for setting wins, losses, corner num
def test_setters() -> None:
    player1 = ComputerPlayer("boby", "b")
    player1.set_corner_num(3)
    assert player1.get_corner_num() == 3
    player1.set_wins(2)
    assert player1.get_wins() == 2
    player1.set_losses(1)
    assert player1.get_losses() == 1
    player2 = ComputerPlayer("justin","lilac", 4, 5, 6)
    player2.set_corner_num(5)
    assert player2.get_corner_num() == 5
    player2.set_wins(7)
    assert player2.get_wins() == 7
    player2.set_losses(8)
    assert player2.get_losses() == 8
    player3 = ComputerPlayer("check", "color", 1, 9, 8)
    player3.set_corner_num(0)
    assert player3.get_corner_num() == 0
    player3.set_wins(0)
    assert player3.get_wins() == 0
    player3.set_losses(0)
    assert player3.get_losses() == 0


# Test for adding wins and losses
def test_add_win_loss() -> None:
    player1 = ComputerPlayer("Charlie", "green")
    player1.add_win()
    player1.add_loss()
    assert player1.get_wins() == 1
    assert player1.get_losses() == 1
    player2 = ComputerPlayer("halie", "orange", 4, 5, 6)
    player2.add_win()
    player2.add_loss()
    assert player2.get_wins() == 6
    assert player2.get_losses() == 7
    player3 = ComputerPlayer("haile", "brown", wins=-8, losses=10)
    player3.add_win()
    player3.add_loss()
    assert player3.get_wins() == -7
    assert player3.get_losses() == 11


# Test for choosing marble coordinates
def test_choose_marble() -> None:
    player1 = ComputerPlayer("Eve", "purple")
    marbles = [(1, 2), (3, 4)]
    chosen_marble = player1.choose_marble(marbles)
    assert chosen_marble in marbles
    player2 = ComputerPlayer("eden", "gray")
    marbles2 = [(0, 0), (-7, 89)]
    chosen_marble = player2.choose_marble(marbles2)
    assert chosen_marble in marbles2
    player3 = ComputerPlayer("john", "blue")
    marbles3 = [(5, 6), (7, 8), (9, 10)]
    chosen_marble = player3.choose_marble(marbles3)
    assert chosen_marble in marbles3


# Test for choosing direction
def test_choose_direction() -> None:
    player1 = ComputerPlayer("Frank", "orange")
    chosen_direction = player1.choose_direction()
    assert chosen_direction in ["ul", "ur", "dl", "dr", "jl", "jr"]
    player2 = ComputerPlayer("koala", "australia")
    chosen_direction = player2.choose_direction()
    assert chosen_direction in ["ul", "ur", "dl", "dr", "jl", "jr"]
    player3 = ComputerPlayer("michael", "yellow")
    chosen_direction = player3.choose_direction()
    assert chosen_direction in ["ul", "ur", "dl", "dr", "jl", "jr"]


# Test for hop choice
def test_hop_choice() -> None:
    player1 = ComputerPlayer("Grace", "cyan")
    hop_choice = player1.hop_choice()
    assert hop_choice in [True, False]
    player2 = ComputerPlayer("emma", "pink")
    hop_choice = player2.hop_choice()
    assert hop_choice in [True, False]
    player3 = ComputerPlayer("lucas", "black")
    hop_choice = player3.hop_choice()
    assert hop_choice in [True, False]

