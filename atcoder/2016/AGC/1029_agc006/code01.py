N = int(input())
s = input()
t = input()

cnt = N
for i in range(N):
    if s[i:] == t[:(N-i)]:
        break
    else:
        cnt -= 1

print((N-cnt)+N)