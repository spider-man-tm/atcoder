N = int(input())
C = input()

red = C.count('R')
white = C.count('W')

left = C[:red]
ans = left.count('W')

print(ans)