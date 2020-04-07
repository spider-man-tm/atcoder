from bisect import bisect_right
 
d = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S',
    'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW', 'N']
x = [11.25 + i * 22.5 for i in range(16)]
y = [0.25, 1.55, 3.35, 5.45, 7.95, 10.75, 13.85, 17.15,
    20.75, 24.45, 28.45, 32.65]
 
deg, dis = map(int, input().split())
deg /= 10
dis /= 60
x = bisect_right(x, deg)
y = bisect_right(y, dis)
print(d[x] if y != 0 else 'C', y)