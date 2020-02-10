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
        
def point_in_circle(circle, point):
    return (point.x - circle.center.x)**2 + (point.y - circle.center.y)**2 < circle.radius**2

def rect_in_circle(circle, rect):
    points = rect.get_points()

    for p in points:
        if not point_in_circle(circle, p):
            return False
    return True

def rect_circle_overlap(circle, rect):
    points = rect.get_points()
    point_found = False

    for p in points:
        if point_in_circle(circle, p):
            point_found = True
    return point_found
    
def main():
    my_circle = Circle(Point(150, 175), 75)
    print('Circle center x coordinate = ' + str(my_circle.center.x))
    my_rectangle = Rectangle()
    print('Corner x coordinate: ' + str(my_rectangle.corner.x))
    print('Corner y coordinate: ' + str(my_rectangle.corner.y))

    in_point = Point(160, 170)
    out_point = Point(0, 0)
    print('Point in circle: ' + str(point_in_circle(my_circle, in_point)))
    print('Point in circle: ' + str(point_in_circle(my_circle, out_point)))

    my_circle = Circle(Point(0, 0), 100)
    in_rect = Rectangle(25, 25)
    out_rect = Rectangle(50, 50)
    
    print('Rect in circle: ' + str(rect_in_circle(my_circle, in_rect)))
    print('Rect in circle: ' + str(rect_in_circle(my_circle, out_rect)))

    print('Rect circle overlap: ' + str(rect_circle_overlap(my_circle, in_rect)))
    print('Rect circle overlap: ' + str(rect_circle_overlap(my_circle, out_rect)))
    

main()
