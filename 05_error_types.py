#####################
# Error Types
#####################

"""

def print_something (something):
    print (something)

try:
    print_something ("Hello World" + 5)

except Exception as e:
    
    print("Se produjo el sgte. error: " + str(e))

"""    
    
## SyntaxError
#print "Hello World"    # Descomentar para Error
print("Hello World")


## NameError   
language = "Python" # Comentar para Error
print(language)


## IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[1])
print(my_list[4])
print(my_list[-1])
#print(my_list[5])   # Descomentar para Error


## ModuleNotFoundError
#import maths    # Descomentar para Error
import math


# AttributeError
#print(math.PI)     # Descomentar para Error
print(math.pi)  


# KeyError   
my_dict = {"Name":"James", "Surname":"Bond", "Age":50, 1:"Python"}
print(my_dict["Name"]) 
#print(my_dict["Agezzzz"])  # Descomentar para Error


# TypeError
#my_list["Name"]     # Descomentar para Error
print(my_list[0])
print(my_list[1:3])
print(my_list[-2])

print(my_list[False])   # Funciona porque traduce False al 
                        # valor 0. Pero no tiene sentido.

print(my_list[True])    # Funciona porque traduce True al
                        # valor 1. Pero no tiene sentido.


try:
    print(my_list["0"])
except TypeError as te:
    print("Cometiste el sgte. error: " + str(te))
    
    
# ImportError
#from math import PI    # Descomentar para Error
from math import pi
print(pi)
    

# ValeError
#my_int = int("10 Years")   # Descomentar para Error
my_int = int("10")
print(type(my_int))


# ZeroDivisionError
#print(4/0)     # Descomentar para Error
print(4/2)

