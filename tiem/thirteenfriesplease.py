import datetime

y = int(input("enter a year (in full): "))
t = datetime.date(y, 1, 13)
c = 0

for i in range(1,13):
    t=datetime.date(y, i, 13)
    if t.weekday() == 4:
        c+=1

print(f"there are {c} friday the 13ths in {y}")