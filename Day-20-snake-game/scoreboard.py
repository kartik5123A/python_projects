from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle() 
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", move = False, align = ALIGNMENT, font = FONT) 

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode = "w") as file:
                file.write(f"{self.high_score}")   
        self.score = 0
        self.update_score()      

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"Game Over!! Your Final Score is {self.score}", align = ALIGNMENT, font = FONT)      

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update_score()    