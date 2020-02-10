import turtle
from shapes import *

def draw_rect(t, rect):
    pass

def draw_circle(t, circle):
    pass

def main():
    win = turtle.Screen()
    win.title('Turtle Circles and Rects')
    win.bgcolor('blue')
    win.setup(width=600, height=600)

    t = turtle.Turtle()
    
    my_circle = Circle(Point(0, 0), 100)
    my_rect = Rectangle()

    draw_circle(t, my_circle)
    draw_rect(t, my_rect)

    win.exitonclick()

main()
