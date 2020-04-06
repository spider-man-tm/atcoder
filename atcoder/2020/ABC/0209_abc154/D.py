n, k = map(int, input().split())
p = list(map(int, input().split()))

p_mean = [(i+1)/2 for i in p]

p_ruikei = [0] * n
p_ruikei[0] =  p_mean[0]

for i in range(1, n):
    p_ruikei[i] = p_ruikei[i-1] + p_mean[i]

maxx = p_ruikei[k-1]
for i in range(1, n-k+1):
    mean = p_ruikei[i+k-1] - p_ruikei[i-1]

    if mean > maxx:
        maxx = mean

print(maxx)