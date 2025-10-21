import numpy as np
from random import randint
# import  matplotlib as plt


def funkcja(x):
    return np.sin(x/10) * np.sin(x/200)

rozrzut = 10
wsp_przyrostu=1.1
l_iteracji=100

x = randint(0, 100)
y = funkcja(x)
for l in range(l_iteracji):
    random_number = randint(int(-rozrzut), int(rozrzut))
    xpot = x + random_number
    if xpot<0:
        xpot = 0
    if xpot>100:
        xpot=100
    ypot = funkcja(xpot)
    if ypot >= y:
        x = xpot
        y = ypot
        rozrzut *= wsp_przyrostu
    if ypot < y:
        rozrzut /= wsp_przyrostu
    print(f"numer iteracji: {l}")
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"rozrzut: {rozrzut}\n\n")
print(x)
