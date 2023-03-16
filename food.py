import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        x = random.randint(-330, 330)
        y = random.randint(-280, 260)
        self.goto(x, y)

    def refresh(self):
        x = random.randint(-330, 330)
        y = random.randint(-280, 260)
        self.goto(x, y)

    def scoreboard(self):
        self.write("Score: ", align="center")
