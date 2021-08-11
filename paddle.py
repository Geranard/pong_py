from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.goto(x, y)
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        x = self.xcor()
        y = self.ycor() + 20
        self.goto(x, y)

    def down(self):
        x = self.xcor()
        y = self.ycor() - 20
        self.goto(x, y)

    def reset_pos(self, x, y):
        self.goto(x, y)
