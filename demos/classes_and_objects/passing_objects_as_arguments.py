class Point:
    '''Represents a point in 2-D space.'''

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle:
    '''Represents a rectangle. 

    attributes: width, height, corner.
    '''

class Circle:
    '''Represents a rectangle. 

    attributes: width, height, corner.
    '''

def update_point(p):
    p.x = 1
    p.y = 1


blank = Point()

'''
Demonstrates the affects aliasing
has on instance state when passing
objects as arguments
'''
print(blank.x)
update_point(blank)
print(blank.x)
