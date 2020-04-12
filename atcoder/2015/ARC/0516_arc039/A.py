A, B = map(int, input().split())
A100 = 900+A%100
B100 = 100+B%100
A10 = A//100*100 + 90 + A%10
B10 = B//100*100 + B%10
A1 = A//10*10 + 9
B1 = B//10*10

a = A - B
a1 = A100 - B
a2 = A10 - B
a3 = A1 - B
a4 = A - B100
a5 = A - B10
a6 = A - B1
print(max(a, a1, a2, a3, a4, a5, a6))