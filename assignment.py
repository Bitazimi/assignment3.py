import random


a = int(input("how many number do you want? "))
n = []

for i in range(a):
    b = (random.randint(1, 100))
    if b not in n:
        n.append(b)


print(n)
