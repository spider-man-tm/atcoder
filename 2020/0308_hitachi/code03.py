n = int(input())
tree = [[] for _ in range(n)]


for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    tree[a].append(b)
    tree[b].append(a)

print(tree)