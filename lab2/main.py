import numpy as np

## Task1
# random freq
p = np.random.randint(1, 10, 10)
print("Frequency:\n", p)

sump = sum(p)

# equation itself - return array
Pis = []
for Pi in p:
    alpha = round(Pi/sump, 3)
    Pis.append(alpha)

print(sum(Pis))
print("P:\n", Pis)

## Task2
# generate random q, but they sum up to 1
wz = np.random.dirichlet(np.ones(10), size=1)

print("Q:\n", wz)
