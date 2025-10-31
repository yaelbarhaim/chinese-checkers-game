from marble import Marble


def test_marble_init() -> None:
    marble1 = Marble("red", (0, 0), 1)
    assert isinstance(marble1, Marble)
    assert marble1.get_color() == "red"
    assert marble1.get_location() == (0, 0)
    assert marble1.get_number() == 1
    marble2 = Marble("PINK", (40, 50), 13)
    assert isinstance(marble2, Marble)
    assert marble2.get_color() == "PINK"
    assert marble2.get_location() == (40, 50)
    assert marble2.get_number() == 13


def test_get_color() -> None:
    marble1 = Marble("R", (0, 0), 1)
    marble2 = Marble("Y", (0, 0), 0)
    marble3 = Marble("W", (1, 1), 2)
    marble4 = Marble("P", (3, 4), 4)
    marble5 = Marble("B", (5, 5), 5)
    marble6 = Marble("G", (2, 2), 6)
    marble7 = Marble("SOWWNSNLK", (3, 3), 7)
    marble8 = Marble("!!!", (4, 4), 99)
    marble9 = Marble("lpp lp", (5, 5), -1)
    marble10 = Marble("333", (6, 6), 25)
    marble11 = Marble("(:", (7, 7), 13)
    marble12 = Marble("", (8, 8), 2)
    marble13 = Marble(4, "R", 3)
    assert marble1.get_color() == "R"
    assert marble2.get_color() == "Y"
    assert marble3.get_color() == "W"
    assert marble4.get_color() == "P"
    assert marble5.get_color() == "B"
    assert marble6.get_color() == "G"
    assert marble7.get_color() == "SOWWNSNLK"
    assert marble8.get_color() == "!!!"
    assert marble9.get_color() == "lpp lp"
    assert marble10.get_color() == "333"
    assert marble11.get_color() == "(:"
    assert marble12.get_color() == ""
    assert marble13.get_color() == 4


def test_get_number() -> None:
    marble1 = Marble("JIJI", (1, 1), 1)
    marble2 = Marble("Y", (700, 3), 2)
    marble3 = Marble("W", (45, 1), 3)
    marble4 = Marble("P", (3, 4), 4)
    marble5 = Marble("B", (5, 0), 5)
    marble6 = Marble("G", (3, 2), 6)
    marble7 = Marble("R", (2, 3), 7)
    marble8 = Marble("B", (0, 0), 8)
    marble9 = Marble("W", (8, 5), 9)
    marble10 = Marble("P", (-3, 6), -50)
    marble11 = Marble("Y", (4, -4), 122)
    marble12 = Marble("K", (0, 9), 9)
    assert marble1.get_number() == 1
    assert marble2.get_number() == 2
    assert marble3.get_number() == 3
    assert marble4.get_number() == 4
    assert marble5.get_number() == 5
    assert marble6.get_number() == 6
    assert marble7.get_number() == 7
    assert marble8.get_number() == 8
    assert marble9.get_number() == 9
    assert marble10.get_number() == -50
    assert marble11.get_number() == 122
    assert marble12.get_number() == 9


def test_get_location() -> None:
    marble1 = Marble("R", (-1, -1), 1)
    marble2 = Marble("Y", (700, 3), 2)
    marble3 = Marble("W", (4.5, 1), 3)
    marble4 = Marble("P", (3, 4), 4)
    marble5 = Marble("B", (5, ""), 5)
    marble6 = Marble("G", (3, 2), 6)
    marble7 = Marble("R", (2.378, 3), 7)
    marble8 = Marble("B", (-0, 0), 8)
    marble9 = Marble("W", (8, 5), 3)
    marble10 = Marble("P", (-3, 6), 0)
    marble11 = Marble("Y", (4, -4), 1)
    marble12 = Marble("K", (0, "k"), 9)
    assert marble1.get_location() == (-1, -1)
    assert marble2.get_location() == (700, 3)
    assert marble3.get_location() == (4.5, 1)
    assert marble4.get_location() == (3, 4)
    assert marble5.get_location() == (5, "")
    assert marble6.get_location() == (3, 2)
    assert marble7.get_location() == (2.378, 3)
    assert marble8.get_location() == (0, 0)
    assert marble9.get_location() == (8, 5)
    assert marble10.get_location() == (-3, 6)
    assert marble11.get_location() == (4, -4)
    assert marble12.get_location() == (0, "k")


def test_set_location() -> None:
    marble1 = Marble("R", (-1, -1), 1)
    marble2 = Marble("Y", (700, 3), 2)
    marble3 = Marble("W", (4.5, 1), 3)
    marble4 = Marble("P", (3, 4), 4)
    marble5 = Marble("B", (5, ""), 5)
    marble6 = Marble("G", (3, 2), 6)
    marble7 = Marble("R", (2.378, 3), 7)
    marble8 = Marble("B", (-0, 0), 8)
    marble9 = Marble("W", (8, 5), 9)
    marble10 = Marble("P", (-3, 6), 0)
    marble11 = Marble("Y", (4, -4), 14)
    marble12 = Marble("K", (0, "k"), 12)
    marble1.set_location((0, 0))
    marble2.set_location((-1, 1))
    marble3.set_location((2, 2.5))
    marble4.set_location((4, 3))
    marble5.set_location((4, 4))
    marble6.set_location((5, 0))
    marble7.set_location((25, 300))
    marble8.set_location(("l", 0))
    marble9.set_location((8, 2))
    marble10.set_location((7, 9))
    marble11.set_location((10, 10))
    marble12.set_location((4, -44))
    assert marble1.get_location() == (0, 0)
    assert marble2.get_location() == (-1, 1)
    assert marble3.get_location() == (2, 2.5)
    assert marble4.get_location() == (4, 3)
    assert marble5.get_location() == (4, 4)
    assert marble6.get_location() == (5, 0)
    assert marble7.get_location() == (25, 300)
    assert marble8.get_location() == ("l", 0)
    assert marble9.get_location() == (8, 2)
    assert marble10.get_location() == (7, 9)
    assert marble11.get_location() == (10, 10)
    assert marble12.get_location() == (4, -44)


def test_step_requirements() -> None:
    marble1 = Marble("red", (2, 2), 4)
    assert marble1.step_requirements("ul") == (1, 1)
    assert marble1.step_requirements("ur") == (1, 3)
    assert marble1.step_requirements("dl") == (3, 1)
    assert marble1.step_requirements("dr") == (3, 3)
    assert marble1.step_requirements("jl") == (2, 0)
    assert marble1.step_requirements("jr") == (2, 4)
    marble2 = Marble("C", (0, 0), 5)
    assert marble2.step_requirements("ul") == (-1, -1)
    assert marble2.step_requirements("ur") == (-1, 1)
    assert marble2.step_requirements("dl") == (1, -1)
    assert marble2.step_requirements("dr") == (1, 1)
    assert marble2.step_requirements("jl") == (0, -2)
    assert marble2.step_requirements("jr") == (0, 2)
    marble3 = Marble("HH", (250, 390), 7)
    assert marble3.step_requirements("ul") == (249, 389)
    assert marble3.step_requirements("ur") == (249, 391)
    assert marble3.step_requirements("dl") == (251, 389)
    assert marble3.step_requirements("dr") == (251, 391)
    assert marble3.step_requirements("jl") == (250, 388)
    assert marble3.step_requirements("jr") == (250, 392)
    marble4 = Marble("P", (-1, -4), 8)
    assert marble4.step_requirements("ul") == (-2, -5)
    assert marble4.step_requirements("ur") == (-2, -3)
    assert marble4.step_requirements("dl") == (0, -5)
    assert marble4.step_requirements("dr") == (0, -3)
    assert marble4.step_requirements("jl") == (-1, -6)
    assert marble4.step_requirements("jr") == (-1, -2)


def test_hop_requirements() -> None:
    marble1 = Marble("red", (4, 4), 1)
    assert marble1.hop_requirements("ul") == (2, 2)
    assert marble1.hop_requirements("ur") == (2, 6)
    assert marble1.hop_requirements("dl") == (6, 2)
    assert marble1.hop_requirements("dr") == (6, 6)
    assert marble1.hop_requirements("jl") == (4, 0)
    assert marble1.hop_requirements("jr") == (4, 8)
    marble2 = Marble("W", (-1, -4), 2)
    assert marble2.hop_requirements("ul") == (-3, -6)
    assert marble2.hop_requirements("ur") == (-3, -2)
    assert marble2.hop_requirements("dl") == (1, -6)
    assert marble2.hop_requirements("dr") == (1, -2)
    assert marble2.hop_requirements("jl") == (-1, -8)
    assert marble2.hop_requirements("jr") == (-1, 0)
    marble3 = Marble("kl", (1.5, 0), 3)
    assert marble3.hop_requirements("ul") == (-0.5, -2)
    assert marble3.hop_requirements("ur") == (-0.5, 2)
    assert marble3.hop_requirements("dl") == (3.5, -2)
    assert marble3.hop_requirements("dr") == (3.5, 2)
    assert marble3.hop_requirements("jl") == (1.5, -4)
    assert marble3.hop_requirements("jr") == (1.5, 4)
