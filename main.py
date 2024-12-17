import time
from turtle import Turtle,Screen
from player import player
from car import Carmanager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

player = player()
car = Carmanager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    #detect collision with car.
    for carmanager in car.all_cars:
        if carmanager.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #detect successful crossing.
    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        scoreboard.increase_level()

screen.exitonclick()
