S = input()
N = int(input())
Ring = [input() for _ in range(N)]

cnt = 0
for w in Ring:
    w += w
    cnt += 1 if w.count(S) else 0

print(cnt)