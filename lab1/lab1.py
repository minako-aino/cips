import random
from datetime import datetime
import numpy as np

def grades(num):
    if num >= 0.9:
        res = 5
    elif num >= 0.7:
        res = 4
    elif num >= 0.5:
        res = 3
    elif num >= 0.3:
        res = 2
    elif num >= 0:
        res = 1

    return res


# Task1
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
          arrayC[a][b][c] = grades(arrayA[a][b][c])

arrayC = arrayC.astype(int)
f.write("\nC:\n")
f.write(str(arrayC))

f.close()

# Task2
# according to the task ¯\_(ツ)_/¯
w1 = 1
w2 = 1
w3 = 1

# case A
sum1 = np.sum(arrayA)
res1 = sum1/140
print(res1)

sum2 = np.sum(arrayB)
res2 = sum2/140
print(res2)
sum3 = np.sum(arrayC)
res3 = sum3/140
res3 = round(res3)
print(res3)
