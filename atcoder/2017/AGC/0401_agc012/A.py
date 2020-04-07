N = int(input())
a = list(map(int, input().split()))
a = sorted(a)

a1, a2, a3 = [], [], []
for i in range(N):
    a1.append(a[i])
    a3.append(a[-(2*i+1)])
    a2.append(a[-(2*i+2)])

print(sum(a2))