import turtle as t
import paddle as p
import ball as b
import time
import scoreboard as sb
import boundry as bry

screen = t.Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.listen()
screen.tracer(0)
boundry = bry.Boundry()
r_paddle = p.Paddle((370, 0))
l_paddle = p.Paddle((-370, 0))  
ball = b.Ball()
scoreboard = sb.Scoreboard()

screen.onkeypress(key = "Up", fun = r_paddle.go_up)
screen.onkeypress(key = "Down", fun = r_paddle.go_down) 

screen.onkeypress(key = "w", fun = l_paddle.go_up)
screen.onkeypress(key = "s", fun = l_paddle.go_down)

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move() 

    #detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    #detect the collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):     
        ball.bounce_x()
        ball.ball_speed *= 0.9

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score_increase()
        ball.ball_speed = 0.1
        
    if ball.xcor() < -380:
        ball.reset_position() 
        scoreboard.r_score_increase()
        ball.ball_speed = 0.1 
        
screen.exitonclick()