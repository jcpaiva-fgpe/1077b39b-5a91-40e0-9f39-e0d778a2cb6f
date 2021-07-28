import calendar
d = input("Date (DD.MM.YYYY)?\n").split('.')
print(calendar.isleap(int(d[-1])))