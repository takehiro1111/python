l = ['sun','mon','tue','wed','thu','fri','sat']

def for_day(week,func):
    for days in week:
        print(func(days))

def sample_day(days):
    return days.capitalize()

for_day(l,sample_day)