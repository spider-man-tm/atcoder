from math import floor

def func(x):
    return floor((x**2 + 4) / 8)

print(func(func(func(20))))