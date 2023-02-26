######################
# Challenges
######################


"""
##### EL FAMOSO FIZZ BUZZ #####
 # Escribe un programa que muestre por consola (con un print) los
 # números de 1 a 100 (ambos incluidos y con un salto de línea entre
 # cada impresión), sustituyendo los siguientes:
 # - Múltiplos de 3 por la palabra "fizz".
 # - Múltiplos de 5 por la palabra "buzz".
 # - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 """
  
def fizz_buzz (from_range, to_range, fizz_number, buzz_number):
    for i in range(from_range, to_range):
        if i % fizz_number == 0 and i % buzz_number == 0:
            print("fizzbuzz")
        elif i % fizz_number == 0:
            print("fizz")
        elif i % buzz_number == 0:
            print("buzz")
        else:
            print(i)

fizz_buzz(90, 101, 3, 5)


"""
##### ¿ES UN ANAGRAMA? #####
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram (word_one, word_two):
    if sorted(word_one.lower()) == sorted(word_two.lower()):
        return True
    else:
        return False


print(is_anagram("WingRoad", "winograd"))


def is_anagram_v2 (word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())


print(is_anagram_v2("WingRoad", "winograd"))


"""
##### LA SUCESIÓN DE FIBONACCI #####
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def calc_fibo(terms):
    
    fibo_list = [0, 1]
    i = 1
    while len(fibo_list) < terms:
        new_element = fibo_list[i] + fibo_list[i - 1]
        fibo_list.append(new_element)
        i += 1
    return fibo_list
    
print(calc_fibo(10))
    

##### Otra manera de calcular Fibonacci ###

def calc_fibo_v2(terms):

    prev = 0
    next = 1

    for i in range(0, terms):
        print(prev)
        old_next = next
        next = prev + old_next
        prev = old_next
    
print(calc_fibo_v2(10))
    
##### Y... Otra manera de calcular Fibonacci ###

def calc_fibo_v3(terms):

    prev = 0
    next = 1

    for i in range(0, terms):
        print(prev)
        fib = prev + next
        prev = next
        next = fib
    
print(calc_fibo_v3(10))

        
"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def is_prime(number):
    nro_divisores = 0
    for i in range (1, (number+1)):
        if (number % i) == 0:
            nro_divisores+=1
            
    if nro_divisores == 2:
        return True
    else:
        return False
        
print(is_prime(11))

list_prime_numbers = list()

for i in range (1, 101):
    if is_prime(i) == True:
        print(i)
        list_prime_numbers.append(i)
        
print(list_prime_numbers)

print("Cantidad de nros primos del 1 al 100:", len(list_prime_numbers))


##### Otra manera de indetificar numeros primos #####


def is_prime_V2():
    
    prime_list = []
    
    for number in range (1, 101):
        
        if number >= 2:
            
            is_divisible = False
            
            for i in range (2, number):
                if number % i == 0:
                    is_divisible = True
                    break
                
            if not is_divisible:
                print(number)
                prime_list.append(number)
    
    return prime_list

prime_list = is_prime_V2()
print("Cantidad de nros primos del 1 al 100:", len(prime_list))


"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def invertir_string(my_string):
    
    j = -1
    
    reversed_string = ""
    for i in range(0, len(my_string)):
        reversed_string = reversed_string + my_string[j]
        j+=-1 
    
    return reversed_string        


print(invertir_string("Terere"))        
                         

##### Otra manera de invertir strings #####

def invertir_string_v2 (my_string):
    
    len_my_string = len(my_string)
    reversed_string = ""
    
    for i in range (0, len_my_string):
        reversed_string += my_string[len_my_string - i - 1]
        
    return reversed_string

print(invertir_string_v2("Terere"))

##### Otras maneras de invertir strings... con slicing #####

language = "Python"
print(language[::-1])

len_lan = len(language)
print(language[-1:(1-len_lan)])

        
"""
FACTORIAL recursivo

"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))


"""
FIBONACCI recursivo

"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))






        