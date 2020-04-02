import itertools

N=int(input())
testimony=[]
for i in range(N):
    a=int(input())
    l=[]
    for j in range(a):
        l2=[int(k) for k in input().split()]
        l.append(l2)
    testimony.append(l)

nums=[0,1]
kind=itertools.product(nums,repeat=N)

def is_corect_kind(k,testimony,N):
    for i in range(N):
        if k[i]==1:
            for t in testimony[i]:
                if k[t[0]-1]!=t[1]:
                    return False
    return True

answer=0
for k in kind:
    if is_corect_kind(k,testimony,N):
        answer=max(answer,sum(k))
print(answer)