# U.S. States Game

This is a simple game that tests your knowledge of U.S. states. It uses the turtle library to display a map of the United States, and prompts you to guess the names of different states.

# Prerequisites

Before running the code, make sure you have the following:

- Python 3 installed
- Required libraries: turtle, pandas
# How to Play

1. Run the code using a Python interpreter.
2. A window will appear displaying a map of the United States.
3. You will be prompted to enter your name. Enter your name in the input box and press Enter to start the game.
4. Guess the names of the states one by one. Enter the name of a state in the input box and press Enter to make a guess.
5. If your guess is correct, the state will be marked on the map, and your score will increase.
6. If your guess is incorrect or you want to exit the game, click the Cancel button or close the window.
7. When the game ends, a message will be displayed showing your score and the states you missed.
# Additional Notes

- The game keeps track of the states you have guessed correctly and writes the remaining states to a CSV file named "missed_states.csv".
- The map and state data are sourced from external files. Make sure you have the following files in the specified locations:
Map image: "../blank_states_img.gif"
State data CSV: "../50_states.csv"
- The game uses the turtle library to display graphics. Click the window to close it after the game ends.
Enjoy playing and testing your knowledge of U.S. states!