#################################################################
# FILE : log.py
# WRITER : yael bar haim , yaelbarhaim , 315232132
# PROJECT : intro2cs final_project 2024
# DESCRIPTION: Log class for "Chinese Checkers"
#################################################################

import helper
import os


class Log:
    """
    Represents a log object - responsible for managing the log file of the game
    Attributes: log_name (Str), log_path (Str)
    Methods include: constructor, add_to_log, read_log etc.
    """

    def __init__(self) -> None:
        """
        A constructor for a Log object.
        :return: None
        """
        helper.logs_folder()     # creates a folder for all games logs (if it doesn't exist)
        self.__log_name = helper.naming_game()
        self.__log_path = os.path.join(os.getcwd(), "logs", self.__log_name)

    def get_log_name(self) -> str:
        """
        Returns the name of the log.
        :return: str, the name of the log
        """
        return self.__log_name

    def set_log_name(self, new_name: str) -> None:
        """
        Changes the name of the log to a new one.
        :param new_name: str, new name fot log
        :return: None
        """
        self.__log_name = new_name
        self.__log_path = os.path.join(os.getcwd(), "logs", self.__log_name)

    def get_log_path(self) -> str:
        """
        Returns the path of the log file
        :return: str, the path of the log file
        """
        return self.__log_path

    def add_to_log(self, message: str) -> None:
        """
        Adds a message to the log file
        :param message: str, message to write
        :return: None
        """
        path = self.get_log_path()
        with open(path, "a") as file:
            file.write(message + "\n")

    def read_log(self) -> None:
        """
        Prints all lines from the log
        :return: None
        """
        with open(self.__log_path, "r") as file:
            content = file.read()
            print(content)
            print("################### END OF GAME LOG ###################" + "\n")
