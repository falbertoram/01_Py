#####################
# Dates
#####################


##### datetime #####
##  https://docs.python.org/3/library/datetime.html#datetime-objects
####################

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


##### time #####
##  https://docs.python.org/3/library/datetime.html#time-objects
################

from datetime import time

current_time = time(21, 10, 6)

print(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)


test_time = time()  # podemos definir un time vacio
print(test_time)    # se imprimiran ceros para time, 
                    # minute y second


##### date #####
##  https://docs.python.org/3/library/datetime.html#date-objects
################

from datetime import date

current_date = date(2023, 2, 2)

print(current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)

print(date.today())
print(date.today().year)
print(date.today().month)
print(date.today().day)

#test_date = date()  # NO nos deja definir un date vacio
#print(test_date)    
                    

## Operaciones

# Modificamos usando date()
current_date = date(current_date.year + 2, current_date.month + 1, 
                    current_date.day + 3)

print(current_date)


diff = now - year_2023  # Dos objetos daytime
                        # definidos mas arriba
print(diff)


diff = current_date - year_2023.date()  # Un objeto date y 
                                        # otro datetime.date
                                        # Tienen que ser del mismo
                                        # tipo o de lo contrario
                                        # no se puede operar
print(diff)


##### timedelta #####
##  https://docs.python.org/3/library/datetime.html#timedelta-objects
#####################

from datetime import timedelta

## Ver ejemplos en la documentacion

time_delta_one = timedelta(weeks = 47)
time_delta_two = timedelta(weeks = 52)
time_delta_three = timedelta(weeks = 43, days = 365)

print(time_delta_one > time_delta_three)

year = timedelta(days = 365)
print(year.total_seconds())





