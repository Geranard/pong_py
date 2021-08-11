from turtle import Turtle
from os import system

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.vx = 10
        self.vy = 10
        self.move_speed = 0.1

    def reset_pos(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1

    def move(self):
        x = self.xcor()+self.vx
        y = self.ycor()+self.vy
        self.goto(x, y)

    def bounce_y(self):
        self.vy *= -1

    def bounce_x(self):
        self.vx *= -1
        self.move_speed *= 0.9

    def info(self):
        x = self.xcor()
        y = self.ycor()
        print(f"({x}, {y})")