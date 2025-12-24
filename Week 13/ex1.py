import datetime as dt
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
date = dt.date(year, month, day)
current_date = dt.date.today()
delta = date - current_date
left = delta.days
if left>0: print(f"You have {left} days left to study!")
elif left==0: print("Good luck! The exam is today.")
else: print(f"The exam was {-left} days ago.")