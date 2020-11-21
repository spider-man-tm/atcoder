from collections import Counter

N, K = map(int, input().split())
S = [input() for _ in range(N)]

C = Counter(S).most_common()
cnt = [0] * len(C)
for i in range(len(C)):
    if C[i][1] == C[K-1][1]:
        cnt[i] = 1

if sum(cnt) > 1:
    print('AMBIGUOUS')
else:
    print(C[K-1][0])
