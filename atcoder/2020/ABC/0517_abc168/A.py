N = input()

if int(N[-1]) in [2,4,5,7,9]:
    print('hon')
elif int(N[-1]) in [0,1,6,8]:
    print('pon')
else:
    print('bon')