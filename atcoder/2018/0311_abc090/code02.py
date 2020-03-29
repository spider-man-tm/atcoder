a, b = map(int, input().split())

count =0
for i in range(a, b+1):
    s1 = str(i)
    if s1==s1[::-1]:
        count += 1

print(count)