import logging
import turtle
import csv
from StateSpot import StateMark
from logs import LogSetup, log_alert

US_IMAGE = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(US_IMAGE)

turtle.shape(US_IMAGE)
turtle.bgcolor("black")

checkmark_state = StateMark()
logs = LogSetup()
log_alert.setLevel(logging.DEBUG)

# Start the Game
Game_on = True
score = 0
states_guessed = []


while Game_on:
    # Player Prompt, output turned to lowercase
    try:
        player_name = screen.textinput(title="Player Info",
                                       prompt="Whats your name?").title().strip()

        if score == 0:
            player_answer = screen.textinput(title="Guess the State?",
                                             prompt="Whats another State's Name?").title().strip()
        elif score == 50:
            Game_on = False
            print("Congratulations! All States have been Checked!")
            screen.clear()
            screen.bye()
            exit()

        else:
            player_answer = screen.textinput(title=f"{score}/50",
                                             prompt="Whats another State's Name?").title().strip()

    except AttributeError or None:
        print("Goodbye! Thanks for playing.")
        screen.clear()
        screen.bye()
        exit()

    if player_answer == '':
        log_alert.debug(f"Player: {player_name} Entered No Answer.")
        continue

    with open("50_states.csv") as s:
        states = csv.reader(s)
        for row in states:
            state = row[0].title()
            if player_answer in state:
                if player_answer not in states_guessed:
                    states_guessed.append(player_answer)
                    score += 1
                x = float(row[1])
                y = float(row[2])
                checkmark_state.checkmark(x, y, player_answer)

turtle.exitonclick()
