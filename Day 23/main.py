import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

frog = Player()
cars = CarManager()
board = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(frog.frog_forward, "Up")
screen.onkey(frog.frog_back, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.make_car()
    cars.move_car()

    #Detect collision with frog and car
    for car in cars.all_cars:
        if car.distance(frog) < 20:
            game_is_on = False
            board.game_over()


    #Detect if user has won the game
    if frog.ycor() > 280:
        board.user_point()
        frog.setposition(0, -280)
        cars.update_speed()






screen.exitonclick()



