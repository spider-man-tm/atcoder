W = int(input())
D = 'DiscoPresentsDiscoveryChannelProgrammingContest2016'

for i in range(len(D)):
    print(D[i], end='')
    if (i + 1) % W == 0 and (i + 1) != len(D):
        print()
    
print()