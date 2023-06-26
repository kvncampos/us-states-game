import turtle
import pandas
from StateSpot import StateMark
from logs import LogSetup, log_alert

checkmark_state = StateMark()
logs = LogSetup()

screen = turtle.Screen()
US_IMAGE = "../blank_states_img.gif"
screen.title("U.S. States Game")
screen.addshape(US_IMAGE)
turtle.shape(US_IMAGE)
turtle.bgcolor("black")

states_data = pandas.read_csv("../50_states.csv")
list_of_states = states_data.state.to_list()

# Start the Game
Game_on = True
score = 0
states_guessed = []

player = None
# Loop to Prevent game from Starting W/O Player Name. 'Exit' keyword Exits the Game.
while not player:
    try:
        player_name = screen.textinput(title="Player Info",
                                       prompt="Whats your name?").title().strip()
        if player_name == 'Exit':
            print("Goodbye! Thanks for playing.")
            screen.clear()
            screen.bye()
            exit()

        elif player_name == '':
            log_alert.debug(f"Player Entered No Name.")
            continue

        elif player_name is not None:
            player = player_name
            break

    except AttributeError or None:
        print("Goodbye! Thanks for playing.")
        screen.clear()
        screen.bye()
        exit()

# Loop for continuing game
while Game_on:

    try:

        if score == 0:
            player_answer = screen.textinput(title="Start of Game: Guess the State?",
                                             prompt="Guess your 1st State's Name?").title().strip()
        elif score == 50:
            Game_on = False
            print("Congratulations! All States have been Checked!")
            screen.clear()
            screen.bye()
            exit()

        else:
            player_answer = screen.textinput(title=f"{score}/50",
                                             prompt="Whats another State's Name?").title().strip()

    # If Player Hits Cancel Button, Game Ends. Prints the Name of Player, Score and Missing States.
    except AttributeError or None:
        print(f"Goodbye {player}! Thanks for playing.")
        print(f"Your Score was {score}/50. Here are the states you missed:")
        df = pandas.read_csv("missed_states.csv")
        state_column = df["States_Missed"]
        print(state_column.to_string(index=False))
        screen.clear()
        screen.bye()
        exit()

    # Check the State from the list_of_states
    if player_answer in list_of_states:
        player_chosen_state = states_data.loc[states_data['state'] == player_answer]

        # Increase the Score only when a New State is guessed.
        if player_answer not in states_guessed:
            states_guessed.append(player_answer)
            score += 1
        # Use the x and y from the chosen state for coordinates
        x = float(player_chosen_state.x.iloc[0])
        y = float(player_chosen_state.y.iloc[0])

        # Use the checkmark to write the name based on coordinates on the map
        checkmark_state.checkmark(x, y, player_answer)

        # Checks states_guessed vs list of states and writes the remaining states in a CSV file.
        set_of_guessed_states = set(states_guessed)
        missing_states = [state for state in list_of_states if state not in set_of_guessed_states]
        missed_states_data = pandas.DataFrame(missing_states, columns=["States_Missed"])
        missed_states_data.to_csv('missed_states.csv', index=False)

    # Logging Section, Logs Blank Inputs and Incorrect Guesses.
    if player_answer == '':
        log_alert.debug(f"Player: {player} Entered No Answer.")
        continue
    elif player_answer not in list_of_states:
        log_alert.debug(f"Player: {player} Entered Incorrect State Not Found in List.")
        continue

turtle.exitonclick()
