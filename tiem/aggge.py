import datetime

b = datetime.date(int(input("enter birth year: ")),int(input("month (number): ")),int(input("day: ")))
t = datetime.date.today()

print(f"youre {(t-b).days} days old")