import random
from datetime import datetime
import numpy as np

# write to a file
f = open("lab1.txt", "a")
f.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
f.write('\n')


# case A
arrayA = np.random.rand(4, 5, 7)
print(arrayA)

# case B
arrayB = np.around(arrayA)
arrayB = arrayB.astype(int)
print(arrayB)

# case C
arrayC = np.empty((4, 5, 7))
for a in range(4):
  for b in range(5):
      for c in range(7):
        if arrayA[a][b][c] >= 0.9:
            arrayC[a][b][c] = 5
        elif arrayA[a][b][c] >= 0.7:
            arrayC[a][b][c] = 4
        elif arrayA[a][b][c] >= 0.5:
            arrayC[a][b][c] = 3
        elif arrayA[a][b][c] >= 0.3:
            arrayC[a][b][c] = 2
        elif arrayA[a][b][c] >= 0:
            arrayC[a][b][c] = 1
arrayC = arrayC.astype(int)
print(arrayC)


"""print("A:\n", array)
f.write(str(array))
f.write('\n')



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
#f.close()

"""