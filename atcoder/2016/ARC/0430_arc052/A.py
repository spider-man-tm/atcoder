S = input()
n = []
for i in S:
    try:
        i = int(i)
        n.append(str(i))
    except ValueError:
        pass

ans = ''.join(n)
print(int(ans))