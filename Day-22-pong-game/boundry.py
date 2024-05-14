from turtle import Turtle

class Boundry(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pensize(6)
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        for _ in range(30):
            self.pendown()
            self.fd(20)
            self.penup()
            self.fd(20)