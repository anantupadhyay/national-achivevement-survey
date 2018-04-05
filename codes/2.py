from datetime import date, timedelta
st_date = date(1990,01,01)
end_date   = date(2000,12, 31)
total_days = (end_date-st_date).days
weeks = total_days/7
days_of_week = {i:weeks for i in range (7)}
if end_date.weekday() > st_date.weekday():
   end_date = end_date.weekday()
else:
   end_date = end_date.weekday() +7

for i in range (st_date.weekday(), end_date + 1):
  days_of_week[i %7] +=1

print ("No of Thursdays are %d" days_of_week[4])