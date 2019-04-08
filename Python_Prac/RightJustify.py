

def right_justify(s):
   s_len = len(s)
   for i in range (70 - s_len):
      print(''),
   print(s)

right_justify('012345678901234567890123456789012345678901234567890123456789')
