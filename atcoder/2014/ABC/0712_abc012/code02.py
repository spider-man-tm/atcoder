n = int(input())

hour = n//3600
amari = n%3600
minute = amari//60
amari = amari%60

hour = str(hour).zfill(2)
minute = str(minute).zfill(2)
second = str(amari).zfill(2)

print('{}:{}:{}'.format(hour, minute, second))