class Point:
    
    '''Represents a point in 2-D space.'''

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

class Circle:

    '''Represents a circle in 2-D space.'''

    def __init__(self, center = Point(), radius = 0.0):
        self.center = center
        self.radius = radius

class Rectangle:

    '''
    Represents a rectangle in 2-D space.
    - width and height represent the rectangle's dimensions
    - corner is a Point object that specifies the lower-left corner of the rectangle
    '''

    def __init__(self, width = 1, height = 1):
        self.width = width
        self.height = height
        self.corner = Point(0, height)

    def get_points(self):
        p1 = self.corner #lower-left corner
        p2 = Point(self.corner.x + self.width, self.corner.y) #lower-right corner
        p3 = Point(self.corner.x, self.corner.y + self.height) #upper-left corner
        p4 = Point(self.corner.x + self.width, self.corner.y + self.height) #upper-right corner
        return [p1, p2, p3, p4]
    
