import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    for x in range(1,6):
        time.sleep(0.1)
        if player.win():
            cars.increase_speed()
            scoreboard.update()
        cars.move_cars()
        screen.update()

        #Detect collisions
        for car in cars.car_list:
            if player.distance(car) < 25:
                game_is_on = False
    cars.spawn_cars()

scoreboard.game_over()
screen.exitonclick()
