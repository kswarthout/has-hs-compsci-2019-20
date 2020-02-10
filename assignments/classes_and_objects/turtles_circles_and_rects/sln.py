import turtle
from shapes import *

def draw_rect(t, rect):
    # Set color and draw rect using its dimensions
    t.color('white')
    for i in range(2):
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)

def draw_circle(t, circle):
    # Change the turtle's position so that the ellipse is drawn
    # with its center at circle's center coordinates
    t.penup()
    t.goto(circle.center.x, circle.center.y - circle.radius)
    t.pendown()

    # Set color and draw using circle's radius
    t.color('white')
    t.circle(circle.radius)

def main():
    win = turtle.Screen()
    win.title('Turtle Circles and Rects')
    win.bgcolor('blue')
    win.setup(width=600, height=600)

    t = turtle.Turtle()
    t.speed(0)

    center_circle = Circle(Point(0, 0), 100)
    non_center_circle = Circle(Point(50, 50), 100)
    draw_circle(t, center_circle)
    draw_circle(t, non_center_circle)
    
    my_rect = Rectangle(100, 100)
    draw_rect(t, my_rect)

    win.exitonclick()

main()
