from swampy.TurtleWorld import *
from math import *

def polygon(t, n, length):
   angle = 360.0 / n
   for i in range(n):
      fd(t, length)
      lt(t, angle)

def circle(t, r):
   angle = 360.0 / 720
   length = 2 * pi * r / 720
   for i in range(720):
      fd(t, length)
      lt(t, angle)
      t.delay = 0.01
      

world = TurtleWorld()
bob = Turtle()
circle(bob, 60)

wait_for_user()

