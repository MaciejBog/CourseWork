from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.speed('fastest')
        self.penup()
        self.goto(0, 250)
        self.color('white')
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", move=False, align='center', font=('Courier', 30, 'normal'))
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", move=False, align='center', font=('Courier', 30, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()