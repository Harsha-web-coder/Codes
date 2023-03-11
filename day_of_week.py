import datetime

date_str = "2023-03-02"  # replace with your desired date string
date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
day_of_week = date_obj.strftime("%A")

print(day_of_week)
