import random
from random import randint
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_time = randint(1, 6)
        if random_time == 1:
            random_y = randint(-260, 260)
            random_color = random.choice(COLORS)
            new_car = Turtle("square")
            new_car.color(random_color)
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move_left(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def next_stage(self):
        self.car_speed += MOVE_INCREMENT

