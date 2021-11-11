#!/usr/bin/env python
# -*-coding:utf-8 -*-
import turtle
import math

# define constants of American flag  
STD_UNIT = 40
# COLOR  
WHITE = "#FFFFFF"
RED = "#B31942"
BLUE = "#0A3161"
# SPECIFICATIONS  
FLAG_HOIST = STD_UNIT*10
FLAG_FLY = FLAG_HOIST*1.9
CANTON_HOIST = FLAG_HOIST*7/13
CANTON_FLY = FLAG_FLY*2/5
ROW_HOIST = CANTON_HOIST/10
COLUMN_FLY = CANTON_FLY/12
STRIPE_WIDTH = FLAG_HOIST/13
STAR_DIAMETER = STRIPE_WIDTH*4/5

def fill_angle(radius):
    """Fill an 5-angle."""
    d = radius/math.sin(math.radians(126))
    side_length = d*math.sin(math.radians(36))
    turtle.left(36)
    turtle.forward(d*math.sin(math.radians(18)))
    turtle.right(54)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(side_length)
        turtle.right(144)
        turtle.forward(side_length)
        turtle.left(72)
    turtle.end_fill()

def main():
    # initialize turtle
    turtle.speed(10)
    turtle.penup()

    # draw the white body
    turtle.fillcolor(WHITE)
    turtle.goto(-FLAG_FLY/2,FLAG_HOIST/2)
    turtle.begin_fill()
    turtle.goto(FLAG_FLY/2,FLAG_HOIST/2)
    turtle.goto(FLAG_FLY/2,-FLAG_HOIST/2)
    turtle.goto(-FLAG_FLY/2,-FLAG_HOIST/2)
    turtle.goto(-FLAG_FLY/2,FLAG_HOIST/2)
    turtle.end_fill()

    # draw the red stripes
    turtle.fillcolor(RED)
    for row in range(0,13,2):
        begin_x = -FLAG_FLY/2
        begin_y = FLAG_HOIST/2 - row*STRIPE_WIDTH
        turtle.goto(begin_x, begin_y)
        turtle.begin_fill()
        turtle.goto(begin_x+FLAG_FLY, begin_y)
        turtle.goto(begin_x+FLAG_FLY, begin_y-STRIPE_WIDTH)
        turtle.goto(begin_x, begin_y-STRIPE_WIDTH)
        turtle.goto(begin_x,begin_y)
        turtle.end_fill()

    # draw the blue canton
    canton_begin_x = -FLAG_FLY/2
    canton_begin_y = FLAG_HOIST/2
    turtle.fillcolor(BLUE)
    turtle.goto(canton_begin_x, canton_begin_y)
    turtle.begin_fill()
    turtle.goto(canton_begin_x+CANTON_FLY, canton_begin_y)
    turtle.goto(canton_begin_x+CANTON_FLY, canton_begin_y-CANTON_HOIST)
    turtle.goto(canton_begin_x, canton_begin_y-CANTON_HOIST)
    turtle.goto(canton_begin_x, canton_begin_y)
    turtle.end_fill()

    # draw the stars
    turtle.fillcolor(WHITE)
    for row in range(1,10):
        star_y = canton_begin_y - ROW_HOIST*row
        for column in range(2-row%2,12,2):
            star_x = canton_begin_x + COLUMN_FLY*column
            turtle.goto(star_x, star_y)
            turtle.seth(90)
            fill_angle(STAR_DIAMETER/2)

    input("Press Enter to continue...")


if __name__=="__main__":
    main()