from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

player_left = Paddle(-350, 0)
player_right = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

keys_pressed = {}

def pressed(event):
    keys_pressed[event.keysym] = True

def released(event):
    keys_pressed[event.keysym] = False

def set_key_binds():
    for key in ["Up", "Down", "w", "s"]:
        screen.getcanvas().bind(f"<KeyPress-{key}>", pressed)
        screen.getcanvas().bind(f"<KeyRelease-{key}>", released)
        keys_pressed[key] = False

screen.listen()
set_key_binds()

still_going = True
while still_going:
    if keys_pressed["w"]: player_left.up()
    if keys_pressed["s"]: player_left.down()
    if keys_pressed["Up"]: player_right.up()
    if keys_pressed["Down"]: player_right.down()
    
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    x = ball.xcor()
    y = ball.ycor()
    distance_p1 = ball.distance(player_left)
    distance_p2 = ball.distance(player_right)

    if ball.ycor()>300 or ball.ycor()<-300:
        ball.bounce_y()
    if (distance_p1<50 or distance_p2<50) and (x>340 or x<-340):
        ball.vx += 1
        ball.vy += 1
        ball.bounce_x()
    
    if x>380:
        player_left.reset_pos(-350, 0)
        ball.reset_pos()
        scoreboard.r_point()
    if x<-380:
        player_right.reset_pos(350, 0)
        ball.reset_pos()
        scoreboard.l_point()

screen.exitonclick()