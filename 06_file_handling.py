########################
# File Handling
########################

# .txt file

import os

## Python file modes
## https://tutorial.eyehunts.com/python/python-file-modes-open-write-append-r-r-w-w-x-etc/

#txt_file = open("01_Py/my_file.txt", "r+")  # Leer y escribir
                                    
#print(txt_file.read()) # Lee e imprime todo el archivo
#print(txt_file.read(10)) # Lee e imprime los diez
                        # primeros caracteres desde donde
                        # esta el cursor

#print(txt_file.readline())  # Lee linea a linea desde donde
                            # esta el cursor
#print(txt_file.readline())

#print(txt_file.readlines()) # Crea una lista cuyos elementos 
                            # son las lineas del archivo 
                            # mas "\n"

#for line in txt_file.readlines():   # Lee e imprime todas
#    print(line)                     # las lineas


#txt_file.read() # Lee todo el archivo y ubica el cursor al final
                # para que en la proxima linea de codigo
                # escribamos una linea mas al archivo
#txt_file.write("\nAunque tambien me gusta JavaScript")

#txt_file.close()    # Es buena practica cerrar el archivo
                    # cuando se termina de trabajar con el

### !!!!!!!!
### Para operaciones Write tener en cuenta donde esta el cursor ###
### !!!!!!!!

#os.remove("01_Py/my_file.txt")  # Eliminar el archivo

txt_file = open("01_Py/my_file.txt", "w+") # Si el archivo existe
                                    # entonces lo abre y lo sobreescribe.
                                    # Si no existe, entonces lo crea y
                                    # empieza a escribir.

txt_file.write("My name is James\nMy surname is Bond\n50 years old") 

txt_file.write("\nMy favourite language is Python")

txt_file.close()    # Es buena practica cerrar el archivo
                    # cuando se termina de trabajar con el

with open("01_Py/my_file.txt", "a") as my_other_file:   # Una manera de
                                                        # hacer append
    my_other_file.write("\nand JavaScript")

txt_file.close()    # Es buena practica cerrar el archivo

txt_file = open("01_Py/my_file.txt", "a")   # Otra manera de 
                                            # hacer append
txt_file.write("\nand Matlab")


"""
My name is James
My surname is Bond
50 years old
My favourite programming languange is Python
Aunque tambien me gusta JavaScript
"""


# .json file

import json

json_file = open("01_Py/my_file.json", "r+") 
## r+ Opens a file for both reading and writing. 
## The file pointer will be at the beginning of the file.

## !!!!!! CUIDADO con w+ !!!!!!
## w+ Opens a file for both writing and reading. 
## Overwrites the existing file if the file exists. 
## If the file does not exist, it creates a new file 
## for reading and writing.

## Python file modes --- IMPORTANTE!!!
## https://tutorial.eyehunts.com/python/python-file-modes-open-write-append-r-r-w-w-x-etc/


#for line in json_file.readlines():   # Lee e imprime todas
#    print(line)                     # las lineas


#print(json_file.readlines()[0:3])
#print(json_file.readline())
#print(json_file.readline())
#print(json_file.readline())

for line in json_file.readlines():
    print(line)

"""
json_test = {
    "Name":"James", 
    "Surname":"Bond",
    "Age":50, 
    "Language":["Python", "JavaScript", "C"],
    "Website":"www.clarin.com"}
"""

#json.dump(json_test, json_file, indent = 2)

json_file.close()

with open("01_Py/my_file.json") as my_other_file:   # No se especifica 
                                                # nigun modo (ej. r/w/a)
                                                # asumiendo que por default
                                                # es read
    for line in my_other_file.readlines():
        print(line)
        
json_dict = json.load(open("01_Py/my_file.json"))   # Recupero lo 
                                                # almacenado en my_file.json
                                                # y lo asigno a una
                                                # variable de tipo dict
print(json_dict)
print(type(json_dict))
print(json_dict["Name"])


# .csv file

### https://www.pythontutorial.net/python-basics/python-write-csv-file/ ###

import csv

csv_file = open("01_Py/my_file.csv", "w+") 

header = ["Name", "Surname", "Age", "Language", "Website"]
data_00 = ["James", "Bond", 50, "Python", "www.clarin.com"]
data_01 = ["Bud", "", 63, "JavaScript", ""]

csv_writer = csv.writer(csv_file)
csv_writer.writerow(header)
csv_writer.writerow(data_00)
csv_writer.writerow(data_01)


csv_file.close()


# .xlsx

import xlrd 



# .xml

import xml




