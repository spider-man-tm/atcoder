n = int(input())
s = input()
total = 0
for i in range(n):
    score = int(69 - ord(s[i]))
    score = 0 if score<0 else score
    total += score

print(total/n)