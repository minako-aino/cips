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
print("Grade A:", grades(a/140))

# case B
b = sum_with_coefs(arrayB, w1, w2, w3)
print("Grade B:",grades(b/140))

# case C
c = np.sum(arrayC)/140
print("Grade C:", round(c))

# Task 3
print("331:", arrayA[2][2][0], arrayB[2][2][0], arrayC[2][2][0])
print("453:", arrayA[3][4][2], arrayB[3][4][2], arrayC[3][4][2])
print("452:", arrayA[3][4][1], arrayB[3][4][1], arrayC[3][4][1])
print("114:", arrayA[0][0][3], arrayB[0][0][3], arrayC[0][0][3])
print("141:", arrayA[0][3][0], arrayB[0][3][0], arrayC[0][3][0])

# Task 5
stuff = []
all_small = a[a < 0.75]
amount = np.count_nonzero(a < 0.75)
print(amount)
for i in all_small:
    arr = np.where(a == i)
    res = [int(x.astype(int)) for x in arr]
    stuff.append(res)

b = np.array(stuff)
for i in range(4):
    print(i + 1, " ", (b[:, 0] == i).sum())
print("-----------")

for i in range(5):
    print(i + 1, " ", (b[:, 1] == i).sum())
print("-----------")

for i in range(7):
    print(i + 1, " ", (b[:, 2] == i).sum())
print("-----------")
