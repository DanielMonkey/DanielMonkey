from math import *

def Hypotenuse(x1, x2):
   lengthsquared = x1**2 + x2**2
   result = sqrt(lengthsquared)
   return result

T_len = Hypotenuse(3, 4)
print 'Length is ', T_len
