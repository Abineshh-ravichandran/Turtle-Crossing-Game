import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.onkeypress(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.display_score()
    car_manager.create_car()
    car_manager.move_cars()

    if player.is_at_finish_line():
        scoreboard.score += 1
        player.restart()
        car_manager.increase_speed()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()

