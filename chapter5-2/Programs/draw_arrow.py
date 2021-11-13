#!/usr/bin/env python
# -*-coding:utf-8 -*-
import turtle
import random
import math


def draw_arrow(begin, end):
    """draw the arrow by begin point and end point"""
    length = ((begin[0] - end[0])**2 + (begin[1]-end[1])**2)**0.5
    arrow_size = length/20

    # draw the line
    turtle.penup()
    turtle.goto(begin)
    turtle.setheading(turtle.towards(end))  # set direction
    turtle.pendown()
    turtle.goto(end)

    # draw the arrow
    turtle.left(150)
    turtle.forward(arrow_size)
    turtle.penup()
    turtle.backward(arrow_size)
    turtle.left(60)
    turtle.pendown()
    turtle.forward(arrow_size)


def main():
    # initialize turtle
    turtle.speed(10)

    # draw axis
    length = 600
    turtle.dot()
    draw_arrow((-length/2, 0), (length/2, 0))
    draw_arrow((0, -length/2), (0, length/2))

    # draw arrow all sides randomly
    turtle.color("blue")
    for _ in range(10):
        arrow_length = random.randrange(0, length/2)
        angle = random.randrange(0, 360)
        draw_arrow((0, 0), (arrow_length*math.cos(angle),
                   arrow_length*math.sin(angle)))

    # exit message
    print("Press Enter to continue...")


if __name__ == "__main__":
    main()
