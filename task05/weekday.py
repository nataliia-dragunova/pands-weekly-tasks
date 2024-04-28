# weekday.py
# a program that outputs whether or not today is a weekday
# author : Nataliia Dragunova


# it showed wrong results :(
'''
import datetime
today = datetime.datetime.today() # today's date
day_of_week = today.weekday() # the day of the week (Monday-Sunday is 0-6)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] # list of days of the week
if days [:5]:
    print("Yes, unfortunately today is a weekday.", days[day_of_week],":(")    
else:
 print("It is the weekend, yay!", days[day_of_week],":)");

'''
# the last version 

import datetime
today = datetime.datetime.today() # today's date
day_of_week = today.weekday() # the day of the week (Monday-Sunday is 0-6)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] # list of days of the week
if day_of_week <= 4:
  print("Yes, unfortunately today is a weekday.", days[day_of_week],":(")      
else:
    print("It is the weekend, yay!", days[day_of_week],":)");


# to check how code works in any day of the week
'''
day_of_week = 3

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] # list of days of the week
if day_of_week <= 4:
  print("Yes, unfortunately today is a weekday.", days[day_of_week],":(")      
else:
    print("It is the weekend, yay!", days[day_of_week],":)");

'''