from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(-280, 260)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Level: {self.score}", font=FONT)

    def game_over(self):
        self.goto(-50, 0)
        self.write("Game Over", font=("Courier", 18, "bold"))
