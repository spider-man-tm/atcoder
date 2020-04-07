X, Y = map(int, input().split())
i = 1

if X%Y==0:
    print(-1)
    exit()
    
while X<=10**18:
    if X*i%Y != 0:
        print(X*i)
        exit()
    else:
        i += 1

print(-1)