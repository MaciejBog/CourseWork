COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
from turtle import Turtle
import random


class CarManager():
    def __init__(self):
        self.car_list = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def spawn_cars(self):
        car = Turtle('square')
        car.shapesize(1,2)
        car.penup()
        car.color(random.choice(COLORS))
        car.goto(320, random.randint(-250,250))
        self.car_list.append(car)


    def move_cars(self):
        for car in self.car_list:
            car.backward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT




