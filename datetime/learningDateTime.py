import datetime
now = datetime.datetime.now()
print(now)

year = now.year
print(year)

diyDateTime = datetime.datetime(2020,8,6,14,20,50)
print(diyDateTime)

fmtDateTime = now.strftime("%Y/%m/%d %H:%m")
print(fmtDateTime)