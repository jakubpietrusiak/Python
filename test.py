import random
b = []

while len(b) < 6:
    c = random.randint(1,49)

    if c in b:
        c = random.randint(1,49)
    else:
        b.append(c)

    print(b)


