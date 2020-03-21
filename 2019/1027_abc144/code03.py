n = int(input())
mini = float('inf')
n_iter = int(n**(1/2)+2)

for i in range(1, n_iter):
    if n%i==0:
        a, b = i, int(n/i)
        dist = (a-1) + (b-1)
        mini = min(mini, dist)

print(mini)