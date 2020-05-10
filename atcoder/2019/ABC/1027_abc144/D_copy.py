import math

a, b, x = map(int, input().split())
s = a*a*b

if x*2 <= s:
    tan = (a * b * b) / (2 * x)
else:
    tan = (2 * (a * a * b - x)) / (a * a * a)

sita = math.degrees(math.atan(tan))
print(sita)