from swampy.TurtleWorld import *
from math import *

#def square(t):
#    for i in range(4):
#        fd(t, 100)
#        lt(t)
def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

#def polygon(t, length, n):
#    angle = 360.0 / n
#    for i in range(n):
#        fd(t, length)
#        lt(t, angle)

def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

#def circle(t, r):
#    circumference = 2 * pi * r
#    n = int(circumference / 3) + 1
#    length = circumference / n
#    polygon(t, length, n)

#def arc(t, r, angle):
#    arc_length = 2 * pi * r * angle / 360
#    n = int(arc_length / 3) + 1
#    step_length = arc_length / n
#    step_angle = float(angle) / n

#    for i in range(n):
#        fd(t, step_length)
#        lt(t, step_angle)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
#print bob

#fd(bob, 100)
#lt(bob)
#fd(bob, 100)
#lt(bob)
#fd(bob, 100)
#lt(bob)
#fd(bob, 100)

#for i in range(4):
#    print 'Hello!'
#    fd(bob, 100)
#    lt(bob)

#square(bob)
#square(bob, 150)
#polygon(bob, 100, 13)
circle(bob, 20)
#arc(bob, 50, 137)
#bob.delay = 0.01
wait_for_user()

