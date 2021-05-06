from swampy.TurtleWorld import *

def polygon(t, n, length):
   angle = 360.0 / n
   for i in range(n):
      fd(t, length)
      lt(t, angle)

world = TurtleWorld()
bob = Turtle()
polygon(bob, 7, 80)

wait_for_user()

