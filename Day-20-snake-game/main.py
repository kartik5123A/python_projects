import turtle as t
import time
import snake as s
import food as f
import scoreboard as sb

screen = t.Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) 

snake = s.Snake()
food = f.Food()
scoreboard = sb.Scoreboard()
screen.update()

screen.listen()
screen.onkey(key = "Up", fun = snake.up) 
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()
    
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_scoreboard()
        snake.reset_snake()
    
    for box in snake.boxes[1:]:
        if snake.head.distance(box) < 10:
           scoreboard.reset_scoreboard()  
           snake.reset_snake() 

screen.exitonclick()  