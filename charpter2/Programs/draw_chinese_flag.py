#!/usr/bin/env python
# -*-coding:utf-8 -*-
import turtle
import math

def draw_angle(radius):
    """Draw an 5-angle."""
    d = radius/math.sin(math.radians(126))
    side_length = d*math.sin(math.radians(36))
    turtle.left(36)
    turtle.forward(d*math.sin(math.radians(18)))
    turtle.right(54)
    turtle.fillcolor("#FFFF01")
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(side_length)
        turtle.right(144)
        turtle.forward(side_length)
        turtle.left(72)
    turtle.end_fill()


def main():
    # unit length for the flag 
    STD_UNIT = 12

    height = 20*STD_UNIT
    width = 30*STD_UNIT
    big_star_radius = 3*STD_UNIT
    small_star_radius = 1*STD_UNIT
    big_star_center = (-10*STD_UNIT, 5*STD_UNIT)
    small_star_center = [(-5*STD_UNIT, 1*STD_UNIT), (-3*STD_UNIT, 3*STD_UNIT), (-3*STD_UNIT, 6*STD_UNIT), (-5*STD_UNIT, 8*STD_UNIT)]

    # draw the background
    turtle.penup()
    turtle.goto(-width/2, height/2)
    turtle.setheading(0)
    turtle.fillcolor("#EE1C25")
    turtle.begin_fill()
    turtle.goto(width/2, height/2)
    turtle.goto(width/2, -height/2)
    turtle.goto(-width/2, -height/2)
    turtle.goto(-width/2, height/2)
    turtle.end_fill()

    # draw the big star
    turtle.goto(big_star_center)
    turtle.setheading(90)
    draw_angle(big_star_radius)

    # draw the small star
    for (x, y) in small_star_center:
        turtle.goto(x, y)
        turtle.setheading(turtle.towards(big_star_center))
        draw_angle(small_star_radius)
    
    input("Press an Enter to continue...")


if __name__ == "__main__":
    main()
