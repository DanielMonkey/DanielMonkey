from swampy.TurtleWorld import *
from math import *

def polygon(t, n, length):
   angle = 360.0 / n
   for i in range(n):
      fd(t, length)
      lt(t, angle)

def circle(t, r):
   circumference = 2 * pi * r
   n = int(circumference / 3) + 1
   angle = 360.0 / n
   length = circumference / n
   for i in range(n):
      fd(t, length)
      lt(t, angle)
      t.delay = 0.01

def arc(t, r, angle):
   length = (2 * pi * r * (angle / 360.0)) / 720
   arc_ang = angle / 720.0
   for i in range(720):
      fd(t, length)
      lt(t, arc_ang)
      t.delay = 0.01      

world = TurtleWorld()
bob = Turtle()
circle(bob, 70)

wait_for_user()

