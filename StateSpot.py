from turtle import Turtle

FONT = ("Arial", 8, "normal")


class StateMark(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def checkmark(self, x, y, state):
        """X and Y Coordinates for Position of State."""
        self.hideturtle()
        self.goto(x, y)
        self.write(state.title(), font=FONT)
