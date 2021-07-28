import calendar
d = input("Date (DD.MM.YYYY)?\n")
print(calendar.isleap(int(d.split('.')[-1])))