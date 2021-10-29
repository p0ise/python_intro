#!/usr/bin/env python
# -*-coding:utf-8 -*-

#!/usr/bin/env python
# -*-coding:utf-8 -*-
import turtle
import math

# the step of x in loop, related to the precision of the graph
STEP_X = 1
# the length of x-y axis
LEN_X = 300
LEN_Y = 300
# the unit for x-y axis
UNIT_X = LEN_X/4
UNIT_Y = LEN_Y/4
# the BOUNDARY of function graph
BOUNDARY = LEN_X//STEP_X*STEP_X/2
FONT = ("Times New Roman", 20, "italic")



def draw_axis(begin, end):
    """draw the axis by begin point and end point"""
    length = ((begin[0] - end[0])**2 + (begin[1]-end[1])**2)**0.5
    arrow_size = length/60

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
    x_begin = (-LEN_X, 0)
    x_end = (LEN_X, 0)

    y_begin = (0, -LEN_Y)
    y_end = (0, LEN_Y)
    
    # initalize the turtle pen
    turtle.speed(10)
    turtle.pensize(1)
    turtle.pencolor("black")
    turtle.penup()

    # draw the x axis
    draw_axis(x_begin, x_end)
    turtle.penup()
    turtle.goto(x_end)
    turtle.write('x',font=FONT)

    # draw the y axis
    draw_axis(y_begin, y_end)
    turtle.penup()
    turtle.goto(y_end)
    turtle.write('y', font=FONT)

    # draw the origin
    turtle.home()
    turtle.dot()
    turtle.write(" 0", font=FONT)

    # label the unit for axis
    cnt = 1
    while cnt<LEN_X/UNIT_X:
        turtle.goto(cnt*UNIT_X, 0)
        turtle.dot()
        turtle.write(cnt, font=FONT)
        turtle.goto(-cnt*UNIT_X, 0)
        turtle.dot()
        turtle.write(-cnt, font=FONT)
        cnt += 1

    cnt = 1
    while cnt<LEN_Y/UNIT_Y:
        turtle.goto(0, cnt*UNIT_Y)
        turtle.dot()
        turtle.write(cnt, font=FONT)
        turtle.goto(0, -cnt*UNIT_Y)
        turtle.dot()
        turtle.write(-cnt, font=FONT)
        cnt += 1

    # draw the quadratic function
    pos_x = -BOUNDARY
    pos_y = UNIT_Y*(pos_x/UNIT_X)**2
    turtle.goto(pos_x, pos_y)
    turtle.pendown()
    pos_x += STEP_X
    while pos_x<=BOUNDARY:
        pos_y = UNIT_Y*(pos_x/UNIT_X)**2
        turtle.goto(pos_x, pos_y)
        pos_x += STEP_X
    turtle.penup()

    input("Press an Enter to continue...")
    


if __name__=="__main__":
    main()