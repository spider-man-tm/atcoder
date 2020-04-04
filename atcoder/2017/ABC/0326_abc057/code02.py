N, M = map(int, input().split())
student = [list(map(int, input().split())) for _ in range(N)]
check = [list(map(int, input().split())) for _ in range(M)]

for s in student:
    dist = float('inf')
    ans = 0
    for i, c in enumerate(check):
        tmp = abs(s[0]-c[0]) + abs(s[1]-c[1])
        if tmp<dist:
            ans = i+1
            dist = tmp
    print(ans)