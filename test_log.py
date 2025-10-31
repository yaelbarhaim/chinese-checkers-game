from log import Log
import os


def test_log_init() -> None:
    new_log = Log()
    assert isinstance(new_log, Log)
    assert "game_" in new_log.get_log_name()
    assert "game_" in new_log.get_log_path()


def test_get_log_name() -> None:
    new_log = Log()
    assert isinstance(new_log.get_log_name(), str)
    assert "game_" in new_log.get_log_name()
    assert ".txt" in new_log.get_log_name()


def test_set_log_name() -> None:
    new_log = Log()
    old_name = new_log.get_log_name()
    new_log.set_log_name("tester")
    new_name = new_log.get_log_name()
    assert isinstance(new_name, str)
    assert new_name == "tester"
    assert old_name != new_name


def test_get_log_path() -> None:
    new_log = Log()
    expected_path = os.path.join(os.getcwd(), "logs", new_log.get_log_name())
    assert new_log.get_log_path() == expected_path


def test_add_to_log() -> None:
    new_log = Log()
    path = new_log.get_log_path()
    new_log.add_to_log("tester")
    assert os.path.exists(path)
    with open(path, "r") as file:
        content = file.read()
        assert "tester" in content
    os.remove(path)
    assert not os.path.exists(path)


def test_read_from_log(capsys) -> None:
    new_log = Log()
    path = new_log.get_log_path()
    new_log.add_to_log("tester")
    expected_output = "tester\n\n################### END OF GAME LOG ###################\n\n"
    new_log.read_log()
    captured = capsys.readouterr()
    assert captured.out == expected_output
    os.remove(path)

