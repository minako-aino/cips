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

def sum_with_coefs(array, w1=1, w2=1, w3=1):
    sum = 0
    for a in range(4):
        sum *= w1
        for b in range(5):
            sum *= w2
            for c in range(7):
                sum *= w3
                sum += array[a][b][c]
    return sum


# case A
a = sum_with_coefs(arrayA, w1, w2, w3)
print(grades(a/140))

# case B
b = sum_with_coefs(arrayB, w1, w2, w3)
print(grades(b/140))

# case C
c = np.sum(arrayC)/140
print(round(c))


#print(res3)

#print(np.sum(np.sum(arrayC, axis = 0))/140)
"""a = np.sum(arrayA[0, :, :]) + np.sum(arrayA[:, :, 0]) + np.sum(arrayA[:, 0, :])
print(arrayA)
print(1)
print(arrayA[0, :, :])
print(grades(a/140))
# case A
sumA1 = w1 * np.sum(arrayA,axis = 0) + w2 * np.sum(arrayA,axis = 1) + w3 * np.sum(arrayA,axis = 2)
print(sumA1)

sumA = np.sum(arrayA)
print(sumA)
#print(sumA/140)
res1 = grades(sumA/140)
print(res1)

sumB = np.sum(arrayB)
#print(sumB/140)
res2 = grades(sumB/140)
print(res2)
"""
"""sum3 = np.sum(arrayC)
print(sum3)
res3 = sum3/140
#print(res3)
res3 = round(res3)
#print(res3)


a = np.sum(arrayC[0, :, :]) + np.sum(arrayC[:, :, 0]) + np.sum(arrayC[:, 0, :])
print(np.sum(arrayC[0, :, :]), np.sum(arrayC[:, :, 0]), np.sum(arrayC[:, 0, :]))

print("-----")
print(a)
#a = round(a/140)
#print(a)"""




