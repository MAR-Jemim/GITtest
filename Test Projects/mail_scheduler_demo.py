import time
from collections import defaultdict

day_length = 1 # 60s in a day :)

leads = iter(range(101, 161))
days = [i for i in range(1, 11)]
followups = [1, 3, 5, 7, 14, 21, 30, 45, 60]
mails_per_day = 3

schedule = defaultdict(dict)


for date in days:
    if 1 not in schedule[date]:
        schedule[date][1] = list() # state 1: waiting followups
    if 2 not in schedule[date]:
        schedule[date][2] = list() # state 2: new leads

    for mail in range(mails_per_day):
        schedule[date][2].append(next(leads))

        for
        # print(next(leads))

# schedule[1] = {'1':6}
print(schedule)