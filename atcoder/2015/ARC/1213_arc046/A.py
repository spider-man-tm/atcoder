N = int(input())

def check(n):
    n = set(str(n))
    if len(n)==1:
        return True
    else:
        return False

cnt = 0
i = 1
while True:
    if check(i):
        cnt += 1
    if cnt==N:
        print(i)
        exit()
    i += 1