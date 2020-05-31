h1, m1, h2, m2, k = map(int, input().split())

start = h1*60 + m1
end = h2*60 + m2

diff = end - start

if diff < k:
    print(0)
else:
    ss = end - k
    print(ss-start)