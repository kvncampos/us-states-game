import turtle
import pandas
from StateSpot import StateMark

checkmark_state = StateMark()

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

player_name = screen.textinput(title="Player Info",
                               prompt="Whats your name?").capitalize().strip()

# Loop for continuing game
while Game_on:

    try:
        if score == 0:
            player_answer = screen.textinput(title="Guess the State?",
                                             prompt="Whats another State's Name?").capitalize().strip()
        elif score == 50:
            Game_on = False
            print("Congratulations! All States have been Checked!")
            screen.clear()
            screen.bye()
            exit()

        else:
            player_answer = screen.textinput(title=f"{score}/50",
                                             prompt="Whats another State's Name?").capitalize().strip()

    # If Player Hits Cancel Button, Game Ends.
    except AttributeError or None:
        print("Goodbye! Thanks for playing.")
        screen.clear()
        screen.bye()
        exit()

    # If Player left answer blank, nothing happens, Game keeps on.
    if player_answer == '':
        continue

    # Check the State from the list_of_states
    if player_answer in list_of_states:
        player_chosen_state = states_data.loc[states_data['state'] == player_answer]
        # print(player_chosen_state)

        # Increase the Score only when a New State is guessed.
        if player_answer not in states_guessed:
            states_guessed.append(player_answer)
            score += 1
        # Use the x and y from the chosen state for coordinates
        x = float(player_chosen_state.x.iloc[0])
        y = float(player_chosen_state.y.iloc[0])

        # use the checkmark to write the name based on coordinates on the map
        checkmark_state.checkmark(x, y, player_answer)

turtle.exitonclick()
