import math
class Point:
    """Represents a point in 2-D space."""

def print_point(p):
    print('(%g, %g)' % (blank.x, blank.y))

def distance_between_points(p1, p2):
    distance = (p2.x - p1.x)**2 + (p2.y - p1.y)**2
    distance = math.sqrt(distance)
    return distance

print Point
blank = Point()
blank2 = Point()
print blank
print blank2
blank.x = 3.0
blank.y = 4.0
print blank.y
x = blank.x
print x
print('(%g, %g)' % (blank.x, blank.y))
distance = math.sqrt(blank.x**2 + blank.y**2)
print distance

print_point(blank)

blank2.x = 7.0
blank2.y = 7.0

print(distance_between_points(blank, blank2))


