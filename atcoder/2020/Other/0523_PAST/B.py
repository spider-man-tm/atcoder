N, M, Q = map(int, input().split())

score = [[] for _ in range(N)]
question = [N]*M

for _ in range(Q):
    s = list(map(int, input().split()))
    if len(s)==3:
        n, m = s[1]-1, s[2]-1
        question[m] -= 1
        score[n].append(m)
    else:
        n = s[1]-1
        ans = 0
        for t in score[n]:
            ans += question[t]
        print(ans)