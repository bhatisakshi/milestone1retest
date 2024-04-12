#Question-5: Python program to print current year,month,day:

import datetime
current_day=datetime.datetime.now()
print("Current year: ",current_day.year)
print("Current month: ",current_day.month)
print("Current day: ",current_day.day)