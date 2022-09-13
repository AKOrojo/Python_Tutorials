from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle(shape="square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(1, 2)
            car.goto(300, random.randint(-250, 250))
            self.all_car.append(car)

    def move_car(self):
        for car in self.all_car:
            new_x = car.xcor() - self.car_speed
            car.goto(new_x, car.ycor())

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
