from datetime import date

Ma, Da = map(int, input().split())
Mb, Db = map(int, input().split())
date1 = date(2012, Ma, Da)
date2 = date(2012, Mb, Db)
print((date2-date1).days)