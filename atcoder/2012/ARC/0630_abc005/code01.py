from collections import Counter

N = int(input())
W = list(input().strip(".").split())

c = Counter(W)
print(c['Takahashikun']+c['takahashikun']+c['TAKAHASHIKUN'])