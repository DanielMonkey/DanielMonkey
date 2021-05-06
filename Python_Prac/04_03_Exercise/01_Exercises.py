from swampy.TurtleWorld import *

def square(t):
   for i in range(4):
      fd(t, 100)
      lt(t)

world = TurtleWorld()
bob = Turtle()
square(bob)

wait_for_user()

