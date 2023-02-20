###############################
# Higher Order Functions
###############################

# A function is called Higher Order Function 
# if it contains other functions as a parameter 
# or returns a function as an output i.e, the 
# functions that operate with another function 
# are known as Higher order Functions.

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5


# Se llama a una funcion dentro de la funcion.
# Esta NO es una higher order function

def sum_two_values_and_add_one(first_value, second_value):
    return sum_one(first_value + second_value)

print(sum_two_values_and_add_one(5, 2))


# Pasamos una funcion como parametro.
# Esta SI es una higher order function

def sum_two_values_and_add_value(first_value, second_value, f):
    return f(first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_one))

print(sum_two_values_and_add_value(5, 2, sum_five))


##### Closures #####

# Funciones que retornan funciones
# SON Higher Order Functions

def sum_ten():
    def add(value):
        return value + 10
    return add  # retorna una funcion

add_closure = sum_ten() # sum_ten() retorna una funcion
print(add_closure(5)) 


def sum_ten (original_value):
    def add (value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(5) # sum_ten() retorna una funcion
print(add_closure(1)) 

print(sum_ten(2)(3))    # Pasamos el parametro para sum_ten
                        # y tambien el parametro para la funcion
                        # add definida dentro de sum_ten


##### Built-in Higher Order Functions #####

# Map -->   necesita un iterable (en este caso la lista 'numbers')
#           al que se le aplica cualquier funcion      

numbers = [2, 5, 10, 21, 3, 30]

def multiply_by_two (number):
    return number * 2

print(list(map(multiply_by_two, numbers))) #Imprimimos como lista
print(tuple(map(multiply_by_two, numbers))) #Imprimimos como tupla
print(set(map(multiply_by_two, numbers))) #Imprimimos como set

print(list(map(lambda value: value * 2, numbers)))  # En este caso
                                            # usamos un lambda
                                            # para no definir una 
                                            # funcion por afuera
                                            
                                            
# Filter

def filter_greater_than_ten (number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))                                        

print(list(map(filter_greater_than_ten, numbers))) # Ver si tiene sentido                                  

print(list(filter(multiply_by_two, numbers))) # Ver si tiene sentido

## Map recorre valores y ejecuta una funcion sobre ellos
## Filter recorre valores y los filtra de alguna manera



# Reduce


##reduce(function, sequence[, initial]) -> value

## Apply a function of two arguments cumulatively 
## to the items of a sequence, from left to right, 
## so as to reduce the sequence to a single value.
## For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) 
## calculates ((((1+2)+3)+4)+5). If initial is present, 
## it is placed before the items of the sequence in 
## the calculation, and serves as a default when 
## the sequence is empty.

from functools import reduce

numbers = [2, 5, 10, 21, 3, 30]
words = ["que ", "tal ", "estamos ", "hoy"]

def sum_two_values (x,y):
    return x + y

print(reduce(sum_two_values, numbers))
print(reduce(sum_two_values, words))
    