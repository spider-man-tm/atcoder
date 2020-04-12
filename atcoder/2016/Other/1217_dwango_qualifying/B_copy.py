T = list(input())
N = len(T)
T1, T2 = T.copy(), T.copy()

for i in range(N):
    if T[i]=='?':
        if i%2==0:
            T1[i] = '2'
            T2[i] = '5'
        else:
            T1[i] = '5'
            T2[i] = '2'    

def cnt(T):
    flag, cnt, ans = 0, 0, 0
    for i in range(N):
        if flag==0:
            if T[i]=='2':
                flag = 2
        elif flag==2:
            if T[i]=='5':
                flag = 5
                cnt += 2
            elif T[i]=='2':
                flag = 2
                cnt = 0
            else:
                flag = 0
                cnt = 0
        elif flag==5:
            if T[i]=='2':
                flag = 2
            else:
                flag = 0
                cnt = 0
        ans = max(ans, cnt)
    return ans

print(max(cnt(T1), cnt(T2)))