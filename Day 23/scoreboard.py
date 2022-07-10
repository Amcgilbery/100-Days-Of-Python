from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-50, 250)
        self.write(f"User level: {self.score}", align="center", font=FONT)

    def user_point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER. Final Level: {self.score}", align="center", font=FONT)


