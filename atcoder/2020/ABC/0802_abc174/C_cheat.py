K = int(input())

a = 7 % K

for i in range(K):
    if a == 0:
        print(i+1)
        exit()
    a = (a * 10 + 7) % K

print(-1)