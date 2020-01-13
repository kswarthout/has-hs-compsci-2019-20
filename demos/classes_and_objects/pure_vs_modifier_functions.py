class Point:
    '''
    A point class
    '''
 
## Pure Function
def get_point(p):
    new_p = Point()
    new_p.x = p.x
    new_p.y = p.y
    return new_p

## Modifier Function
def update_point(p):
    p.x = p.x + 1
    p.y = p.y + 1

p1 = Point()
p1.x = 3.0
p1.y = 4.0
p2 = get_point(p1)
update_point(p1)
