#!/usr/bin/env python
# -*-coding:utf-8 -*-

import turtle
import math

def draw_polygon(n, distance=100):
    """Draw an n-sided polygon."""
    degree_of_inner_angle = (n-2)*180/n
    side_length = 2*distance*math.sin(math.radians((180-degree_of_inner_angle)/2))
    turtle.penup()
    turtle.forward(distance)
    turtle.right(180-degree_of_inner_angle/2)
    turtle.pendown()
    for _ in range(n):
        turtle.forward(side_length)
        turtle.right(180-degree_of_inner_angle)
    turtle.penup()

def draw_angle(n, distance=100):
    """Draw an n-angle."""
    degree = 360/n
    side_length = distance*math.sin(math.radians(degree/2))/math.cos(math.radians(degree))
    turtle.penup()
    turtle.forward(distance)
    turtle.right((180-degree)/2)
    turtle.pendown()
    for _ in range(n):
        turtle.forward(side_length)
        turtle.right(2*degree)
        turtle.forward(side_length)
        turtle.left(degree)
    turtle.penup()

def draw_shape1(distance=100):
    """绘制不规则图形1"""
    for i in range(1,7):
        turtle.penup()
        turtle.forward(distance)
        turtle.right(90)
        draw_polygon(4, distance)
        turtle.home()
        turtle.right(360/6*i)

def draw_shape2(distance=100):
    """绘制不规则图形2"""
    degree = 360/9
    for i in range(1,10):
        turtle.penup()
        turtle.forward(distance)
        turtle.right(90)
        draw_polygon(4, distance*math.tan(math.radians(degree/2)))
        turtle.home()
        turtle.right(degree*i)

def draw_shape3(distance=100):
    """绘制不规则图形3"""
    degree = 360/8
    side_length = 2*distance*math.sin(math.radians(degree/2))
    turtle.home()
    for i in range(1,9):
        turtle.penup()
        turtle.forward(distance*math.cos(math.radians(degree/2))+side_length/3**0.5/2)
        draw_polygon(3, side_length/3**0.5)
        turtle.home()
        turtle.right(degree*i)
        
def draw_shape4(distance=100):
    """绘制五角星"""
    draw_angle(5, distance)

def main():
    pass
    input("Press any key to continue...")

if __name__=="__main__":
    main()