import math
import copy

class Point:
    """Represents a point in 2-D space."""

class Rectangle:
    """Represents a rectangle.
    attributes: width, height, corner."""

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

def distance_between_points(p1, p2):
    distance = (p2.x - p1.x)**2 + (p2.y - p1.y)**2
    distance = math.sqrt(distance)
    return distance

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width / 2
    p.y = rect.corner.y + rect.height / 2
    return p

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

def move_rectangle(rect, dx, dy):
    #rect.corner.x += dx
    #rect.corner.y += dy
    box_temp = copy.deepcopy(rect)
    box_temp.corner.x += dx
    box_temp.corner.y += dy
    return box_temp


print(Point)
blank = Point()
blank2 = Point()
print(blank)
print(blank2)
blank.x = 3.0
blank.y = 4.0
print(blank.y)
x = blank.x
print(x)
print('(%g, %g)' % (blank.x, blank.y))
distance = math.sqrt(blank.x**2 + blank.y**2)
print(distance)

print_point(blank)

blank2.x = 7.0
blank2.y = 7.0

print(distance_between_points(blank, blank2))

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

center = find_center(box)
print_point(center)
#print(center.x)
#print(center.y)

print(box.width, box.height)
grow_rectangle(box, 50, 100)
print(box.width, box.height)


print_point(box.corner)
temp_rect = Rectangle()
temp_rect = move_rectangle(box, 50, 100)
print_point(temp_rect.corner)
print_point(box.corner)

p1 = Point()
p1.x = 3.0
p1.y = 4.0
p2 = copy.copy(p1)
print_point(p1)
print_point(p2)
print(p1 is p2)
print(p1 == p2)
#print(p1.z)
#print(type(p1))
print('Here1')
print(isinstance(p1, Point))
print(hasattr(p1, 'x'))
print(hasattr(p1, 'z'))


box2 = copy.copy(box)
print(box2 is box)
print(box2.corner is box.corner)

box3 = copy.deepcopy(box)
print(box3 is box)
print(box3.corner is box.corner)





