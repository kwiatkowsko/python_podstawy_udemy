days = ['mon','tue','wed','thu','fri','sat','sun']
print(days)
workdays = days.copy()
workdays.remove("sat")
workdays.remove("sun")
print(workdays)
