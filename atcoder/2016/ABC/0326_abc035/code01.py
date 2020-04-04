w, h = map(int, input().split())

asp = w/h

if 1.3 < asp < 1.4:
    print('4:3')
else:
    print('16:9')