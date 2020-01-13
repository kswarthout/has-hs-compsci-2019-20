class Point:
    '''
    A point class
    '''

p1 = Point()
p1.x = 7
p2 = p1

## Both references refer to
## the same object
print(p1.x)
print(p2.x)

## When we update the value of
## one object, it effects the
## value of any aliased references
p1.x = 8

print(p1.x)
print(p2.x)
