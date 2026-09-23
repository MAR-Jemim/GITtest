import time
from collections import defaultdict, deque
import heapq as hq

### functions
# discontinue -> deletes all follow-ups
# do -> to do require task

day_length = 1 # 60s in a day :)

leads = iter(range(1000001, 1000500))
days = [i for i in range(91)]
followups = [0,  2,  4,  6, 13, 20, 29,  44,  59]
fl_scores = [0, 20, 30, 40, 55, 70, 90, 110, 140]
fl_length = len(followups)
mails_per_day = 8
extra_mail = 2
neg_score = 8

discontinued = set()

schedule = defaultdict(list)


### FUNCTIONS ###
# do
def do(lead, sl=None):
    print(f"{sl:>02d}|" if sl else ' ', lead)

# show : this is to show the rest of the schedule
def show(s=schedule):
    for i in range(59 + len(days)):
        if i in s:
            print(f"   <{i:02d}>")
            print(*s[i])
            print()

# main task
for day in days:
    print(f"DAY: {day:02d}")

    if not schedule[day]:
        for mail in range(mails_per_day):
            lead = next(leads)
            for i in range(fl_length):
                schedule[day+followups[i]].append([fl_scores[i], lead, i+1]) # [score, lead_mail, nth-mail]
        # continue

    mails = schedule[day]
    mails.sort()
    max_mails = mails_per_day + (extra_mail if len(mails) > 2 * mails_per_day else 0)
    for m in range(len(mails)):
        if m < max_mails:
            do(mails[m], m+1)
        else:
            mails[m][0] -= neg_score
            schedule[day+1].append(mails[m])
            # schedule[day][mails[m]]
    print()

    del schedule[day]


# show()