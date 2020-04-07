N = int(input())
s = input()
r = s.count('R')
b = s.count('B')

ans = 'Yes' if r>b else 'No'
print(ans)