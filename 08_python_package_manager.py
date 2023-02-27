##############################
# Python Package Manager
##############################

# !!!!!!!!!!!!!
# Un package es un conjunto de modulos
# !!!!!!!!!!!!!

# PIP https://pypi.org/

# En la consola:
#
# pip install pip
# pip --version


# pip install numpy
import pandas
from mypackage import arithmetics
import requests
import numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)

# pip install pandas

# pip list
# pip uninstall pandas
# pip show numpy    # Devuelve info sobre numpy

# pip install requests

#response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
#print(response)
#print(response.status_code)
#print(response.json())

# Arithmetics Package
# el modulo __init__.py dentro del package
# es necesario para que precisamente se 
# comporte como un paquete. Esto es muy importante
# si lo vamos a compartir. Si trabajo localmente y nadie 
# lo va a acceder, no haria falta

print(arithmetics.sum_two_values(1, 4))
