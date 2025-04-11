Chinese Checkers (Python Project)

This is a Python implementation of the board game Chinese Checkers, developed as part of a university course in computer science. The project includes a fully playable version of the game in the console, with multiple enhancements that improve gameplay, usability, and functionality.

About the Game
Chinese Checkers is a strategy board game that can be played by two to six players. The objective is to move all of your marbles from your home triangle to the opposite triangle on the board before your opponents do. Players can move their pieces one step at a time or use multiple jumps over adjacent pieces, which introduces strategic planning and positioning.

In this project, I implemented both the standard version of the game and a "capture" variant, along with several advanced features and enhancements to enrich the playing experience.

Features and Extensions
This project includes several original extensions I implemented beyond the course requirements:

1. "Capture" Version of the Game
On every run of main.py, the user is prompted to choose between the standard game and a Capture Mode.

Capture Mode includes modified rules, introducing an additional layer of complexity and strategy.

2. Pytest Tests
All tests are implemented using Pytest, located in the main directory.

Tests include:

Validation of user inputs (valid and invalid).

Simulation of sequences of inputs using monkeypatch.

Output capture and verification using capsys.

3. Sound Effects
Audio effects are integrated into different parts of the game for a more immersive experience.

Sound files are located in the sounds folder and are automatically loaded each time the game runs.

4. Color-Coded Gameplay
Game pieces are color-coded based on player selection using the colorama library.

Enhances user experience by:

Making it easier to identify marbles on the board.

Simplifying marble selection (e.g., by typing a digit corresponding to a colored marble).

5. Type Annotations
Type hints are used throughout the codebase for better readability and maintainability.

6. Interactive Log File Reading
In addition to the standard log file recording, the program supports real-time log reading.

At the start of any local player’s turn, entering 'logs' allows the player to:

Select and view a log file (e.g., to study a strategy mid-game).

Seamlessly return to the game from the exact point it was paused.

Make sure you have Python 3.10+ installed.



What I Learned
This project helped me strengthen my skills in:

Object-oriented programming

User interaction and interface design

Writing robust and flexible test suites

Using third-party libraries (colorama, pytest, playsound, etc.)

Handling I/O and logs mid-execution in a smooth and user-friendly way

