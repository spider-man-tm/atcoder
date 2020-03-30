a, b = map(int, input().split())

for p in range(10**4):
    tax8 = p*0.08
    tax10 = p*0.1

    if int(tax8)==a and int(tax10)==b:
        print(p)
        exit()

print(-1)