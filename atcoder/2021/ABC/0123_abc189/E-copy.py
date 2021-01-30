import sys

def xp(p):
    return [[-1, 0, 2 * p], [0, 1, 0], [0, 0, 1]]

def yp(p):
    return [[1, 0, 0], [0, -1, 2 * p], [0, 0, 1]]

def mult(A, B):
    C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            C[i][j] = A[i][0] * B[0][j] + A[i][1] * B[1][j] + A[i][2] * B[2][j]
    return C

def solve():
    input=sys.stdin.readline
    N = int(input())
    P = [[int(x) for x in input().split()] for _ in range(N)]
    M = int(input())
    pos = [None for _ in range(M + 1)]
    pos[0] = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    r = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]
    l = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
    for i in range(M):
        op = input().strip("\n").split()
        if op[0] == "1": pos[i+1] = mult(r, pos[i])
        elif op[0] == "2": pos[i+1] = mult(l, pos[i])
        elif op[0] == "3": pos[i+1] = mult(xp(int(op[1])), pos[i])
        else: pos[i+1] = mult(yp(int(op[1])), pos[i])
    
    Q = int(input())
    ans = [[0, 0] for _ in range(Q)]
    for i in range(Q):
        a, b = map(int, input().split())
        x, y = P[b-1]
        D = pos[a]
        ans[i][0] = D[0][0] * x + D[0][1] * y + D[0][2]
        ans[i][1] = D[1][0] * x + D[1][1] * y + D[1][2]
    
    for a in ans: print(*a)
   
    return 0

if __name__ == "__main__":
    solve()