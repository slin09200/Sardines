import random
import turtle
import numpy as np

def init_sardines(sardine_list):
    for fish in sardine_list:
        rand_X_coord = np.random.uniform(- screen.window_width() / 2.3, screen.window_width() / 2.3)
        rand_Y_coord = np.random.uniform(- screen.window_height() / 2.3, screen.window_height() / 2.3)
        rand_heading = np.random.uniform(0, 359)
        fish.setx(rand_X_coord)
        fish.sety(rand_Y_coord)
        fish.setheading(rand_heading)
        turtle.color('deep sky blue')
        turtle.write("spawning fish", align='center', font=("Arial", "18", "normal"))
    turtle.clear()
    for fish in sardine_list:
        fish.showturtle()

def perpetual_random_motion(sardine_list):
    x_ub = (screen.window_width() / 2) - 50
    x_lb = (- screen.window_width() / 2) + 50
    y_ub = (screen.window_height() / 2) - 50
    y_lb = (- screen.window_height() / 2) + 50
    while True:
        for fish in sardine_list:
            fish.forward(10)
            print(fish.xcor(), fish.ycor(), fish.heading())
            if fish.xcor() > x_ub:
                if 0 <= fish.heading() <= 90:
                    fish.left(60)
                if 270 <= fish.heading() <= 360:
                    fish.right(60)
            elif fish.xcor() < x_lb:
                if 90 <= fish.heading() <= 180:
                    fish.right(60)
                if 180 <= fish.heading() <= 270:
                    fish.left(60)
            elif fish.ycor() > y_ub:
                if 0 <= fish.heading() <= 90:
                    fish.right(60)
                if 90 <= fish.heading() <= 180:
                    fish.left(60)
            elif fish.ycor() < y_lb:
                if 270 <= fish.heading() <= 360:
                    fish.left(60)
                if 180 <= fish.heading() <= 270:
                    fish.right(60)
            else:
                fish.left(np.random.uniform(-15, 15))
'''
def n_nearest_neighbors(sardine_list, fishy):
    min_distance = screen.window_width() + screen.window_height()
    for fish in sardine_list:
'''


if __name__ == '__main__':
    screen = turtle.Screen()
    screen.bgpic('ocean.gif')
    screen.setup(852, 480)
    screen.screensize(852, 480)
    screen.update()
    sardine = ((0, 0), (5, 0), (2, 5), (5, 12), (0, 20), (-5, 12), (-2, 5), (-5, 0))
    turtle.register_shape('sardine', sardine)
    num_sardines = int(input("How many sardines in your school? : "))
    sardine_list = []
    colors = ['springgreen', 'cyan', 'red', 'yellow', 'violet', 'dark orange']
    for i in np.arange(num_sardines):
        fish = turtle.Turtle(shape='sardine', visible=False)
        fish.color(colors[int(np.random.uniform(0, 6))])
        fish.penup()
        sardine_list.append(fish)
    init_sardines(sardine_list)
    perpetual_random_motion(sardine_list)
