n = int(input())
ryuka = [0] * (n+1)

for i in range(n+1):
    if i==0:
        ryuka[i] = 2
    elif i==1:
        ryuka[i] = 1
    else:
        ryuka[i] = ryuka[i-2] + ryuka[i-1]

print(ryuka[-1])