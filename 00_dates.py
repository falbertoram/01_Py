#####################
# Dates
#####################

from datetime import datetime

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second) 
    print(date.timestamp())

now = datetime.now()

#print(now)

print_date(now)

#print(now.year)
#print(now.month)
#print(now.day)
#print(now.hour)
#print(now.minute)
#print(now.second)

#timestamp = now.timestamp() # Since 1970

#print(timestamp)

year_2023 = datetime(2023, 1, 1)
print_date(year_2023)









