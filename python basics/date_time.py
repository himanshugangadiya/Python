from datetime import datetime


x= datetime.now()

date  = x.day
month  = x.month
year  = x.year

hours=x.hour
minutes =x.minute
seconds =x.second
am_pm = x.strftime('%p')

print(date,month,year, sep='-')
print(hours,':',minutes,':',seconds,":",am_pm)
