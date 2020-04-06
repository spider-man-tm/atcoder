n = int(input())
s = input()
num=s.count("E")
length=len(s)

ans = num
for i in range(length):
    if s[i]=="W":
        num +=1
    elif s[i]=="E":
        num -=1

    ans = min(ans, num)

print(ans)