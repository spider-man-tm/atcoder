n = int(input())
x = list(map(int, input().split()))

x_sort = sorted(x)

med1_ix = n//2-1
med2_ix = n//2

med1 = x_sort[med1_ix]
med2 = x_sort[med2_ix]

for i in x:
    if i <= med1:
        print(med2)
    else:
        print(med1)