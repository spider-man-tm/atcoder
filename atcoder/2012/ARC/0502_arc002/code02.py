import datetime
d = input()
t = datetime.datetime.strptime(d, '%Y/%m/%d')


def ok(tm):
    if tm.year % (tm.month * tm.day) == 0:
        return True
    return False
 
while True:
    if ok(t):
        print(t.strftime('%Y/%m/%d'))
        break
    t = t + datetime.timedelta(days=1)