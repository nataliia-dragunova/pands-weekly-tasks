# weekday.py
# a program that outputs whether or not today is a weekday
# author : Nataliia Dragunova

import datetime
today = datetime.datetime.today() # today's date
day_of_week = today.weekday() # the day of the week (Monday is 0, Sunday is 6)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] # list of days of the week
if days [-1:] or days[-2:]:
    print("It is the weekend, yay!", days[day_of_week],":)")
else:
    print("Yes, unfortunately today is a weekday.", days[day_of_week],":(");