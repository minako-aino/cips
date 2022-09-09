import random
from datetime import datetime
import numpy as np

# write to a file
f = open("lab1.txt", "a")
f.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
f.write('\n')


array3 = np.random.rand(4, 5, 7)
print(array3)
"""
# case A
array = [[[random.random() for col in range(4)] for col in range(5)] for row in range(7)]
print("A:\n", array)
f.write(str(array))
f.write('\n')

# case B
array = 1
for a in range(7):
  for b in range(5):
      for c in range(4):
        array[a][b][c] = round(array[a][b][c])
print("B:\n", array)
f.write(str(array))
f.write('\n')

# case C
for a in range(7):
  for b in range(5):
      for c in range(4):
        if array1[a][b][c] >= 0.9:
            array1[a][b][c]

#f.write()
#f.close()"""

