from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')

class Scoarboard(Turtle):
    def __init__(self):
        super(Scoarboard, self).__init__()
        self.score = 0
        self.goto(x=0, y=270)
        self.hideturtle()
        self.color("white")
        self.updated_scoreboard()

    def updated_scoreboard(self):
            self.write(f"Score: {self.score}", align=ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.updated_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font= FONT)
