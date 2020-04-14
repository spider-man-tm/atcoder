from fractions import gcd

N = int(int(input()))
A = list(map(int, input().split()))

left, right = [0], [0]
for i in range(N-1):
    left += [gcd(left[i], A[i])]
    right += [gcd(right[i], A[-1-i])]

right = right[::-1]

print(left)
print(right)
print()
ans = 0
for i in range(N):
    print(left[i], right[i], gcd(left[i], right[i]))
    ans = max(ans, gcd(left[i], right[i]))

print(ans)