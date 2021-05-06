from math import *

def distance(x1, y1, x2, y2):
   dx = x2 - x1
   dy = y2 - y1
   dsquared = dx**2 + dy**2
   result = sqrt(dsquared)
   return result

d = distance(1, 2, 4, 6)
print 'Distance is ', d



