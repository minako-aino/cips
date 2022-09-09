import random
from datetime import datetime
import numpy as np

# write to a file
f = open("lab1.txt", "a")
f.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


# case A
arrayA = np.random.rand(4, 5, 7)

f.write("\nA:\n")
f.write(str(arrayA))


# case B
arrayB = np.around(arrayA)
arrayB = arrayB.astype(int)

f.write("\nB:\n")
f.write(str(arrayB))

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
f.write("\nC:\n")
f.write(str(arrayC))

f.close()
