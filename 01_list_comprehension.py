########################
# List Comprehension
########################

my_original_list = [35, 24, 62, 52, 30, 30, 17]

my_list = [i for i in my_original_list]
print(my_list)


my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_list = [i for i in range(8)] # Una forma de crear una lista
print(my_list)

my_range = range(8) # Otra forma de crear una lista
print(list(my_range))


my_list = [i + 1 for i in range(8)] # Suma 1 antes de agregar el
                                    # elemento a la lista
print(my_list)


my_list = [i * 2 for i in range(8)] # multiplica por 2 antes de agregar el
                                    # elemento a la lista
print(my_list)


my_list = [i * i for i in range(8)] # Multiplica por si mismo antes 
                                    # de agregar el elemento a la lista
print(my_list)


def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)] # Aplicamos una funcion
print(my_list)


