X = int(input())
n500 = X//500
mod = X%500
n5 = mod//5

print(n500*1000 + n5*5)