from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)
scores=Score()
snake= Snake()
food=Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()
game_is_on= True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision of food
    if snake.head.distance(food) <15:
        food.refresh()
        scores.scoreRefresh()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor()<-280 or snake.head.ycor() > 280 or snake.head.ycor()<-280 :
        scores.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if segment==snake.head:
            snake.reset()
        elif snake.head.distance(segment)<10:
            scores.reset()
            snake.reset()









screen.exitonclick()