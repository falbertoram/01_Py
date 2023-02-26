############################
# Regular Expressions
############################

import re

##### match #####
#################
#################

my_string = "Esta es la leccion numero 7: Leccion Expresiones Regulares"
my_other_string = "Esta no es la leccion numero 6: Manejo de ficheros"

print(re.match("esta es la leccion", my_string))
print(re.match("Expresiones Regulares", my_string)) # el string esta
                                            # en my_string pero como
                                            # match solo busca desde 
                                            # el inicio, entonces
                                            # no devuelve nada
                                            
match = re.match("esta es la leccion", my_string, re.I)  # re.I ignora
                                                        # el case
                                                        # VER OTROS FLAGS!!

span = match.span() # Devuelve el rango en donde
                    # encontro el string

print(match)

print(span) 
print(type(span))   # Es una tupla

start, end = span  # Desacoplo la tupla en
                # esas dos variables,
                # start y end
                
print(start, end) 

print(my_string[start:end])  # Imprime solo la parte de
                             # my string que hizo match                    


match = re.match("esta es la leccion", my_string, re.I)  # re.I ignora
                                                         # el case
print(match)    # Si no se hace match, entonces
                # match == None, por tanto
                # debemos controlar eso antes de 
                # imprimir o hacer otra operacion
                 
if not(match == None):
#if match != None:    # Otra manera de comprobar
                      # el None    
#if match is not None:    # Y otra manera de comprobar
                          # el None            
    print(match)
    span = match.span()
    start, end = span 
    print(my_string[start:end])           
else:
    print("No se hizo match")


##### search #####
##################
##################

# A diferencia de match que busca solo desde el inicio, search
# puede verificar si el string buscado se encuentra en cualquier 
# posicion del string evaluado.

search = re.search("numero 7", my_string, re.I)  # re.I ignora
                                                 # el case
print(search)    # Retorna el match y el span

start, end = search.span()
print(start, end)
print(my_string[start:end])
                                                        
                                                        
##### findall #####
###################
###################

findall = re.findall("leccion", my_string, re.I)
print(findall)


##### split #####
#################
#################

split = re.split(":TT", my_string)    # Devuelve una lista
                                # con elementos separados 
                                # por el pattern ":"
                                # Si no encuentra el pattern
                                # entonces retorna un solo 
                                # elemento en la lista (el string
                                # completo sin separar nada)
                                
print(split)


##### sub #####
###############
###############

print(re.sub("leccion", "LECCION", my_string))

print(re.sub("Expresiones Regulares", "RegEx", my_string))

print(re.sub("leccion|Leccion", "LECCION", my_string)) # Con el pipe |
                                                # agregamos otros 
                                                # strings a ser cambiados
                                                
print(re.sub("[lL]eccion", "LECCION", my_string)) # Hace lo mismo que
                                            # la linea anterior

# !!!!!!!!!!                                            
# REPASAR EXPRESIONES REGULARES
# EN 30_days_of_Python
# !!!!!!!!!!                                            


##### Patterns #####

pattern = r"[Ll]eccion"    # En Python definimos un pattern
                            # con una r 

print(re.findall(pattern, my_string)) 

pattern = r"[Ll]eccion|Expresiones" # Usando el pipe | podemos
                            # definir mas de un pattern a ser 
                            # buscado
                            
print(re.findall(pattern, my_string))   

pattern = r"[a-z]"  # Todas las ocurrencias de la 'a' a la 'z'
                    # porque usamos re.findall en la sgte. linea
print(re.findall(pattern, my_string))                         

pattern = r"[a-z]"  # Devuelve solamente la 's' porque
                    # usamos re.search en la sgte. linea
print(re.search(pattern, my_string))                         
   
pattern = r"[0-9]"  # Todas las ocurrencias del '0' al '9'
                    # Solo devuelve el '7' en el caso de
                    # my_string
print(re.findall(pattern, my_string))                         
                                             

pattern = r"[0-5]"  # Devuelve una lista vacia
print(re.findall(pattern, my_string))   


pattern = r"\d" # Devuelve los digitos encontrados en my_string
print(re.findall(pattern, my_string))   


pattern = r"\D" # Devuelve todos los caracteres que NO son 
                # digitos en my_string
print(re.findall(pattern, my_string))   


pattern = "[l]." # Devuelve todas las ocurrencias de 'l' y el 
                 # siguiente caracter que encuentra
print(re.findall(pattern, my_string))   

                      
pattern = "[l].*" # Devuelve la 'l' y todo los caracteres que 
                  # encuentra despues de la 'l'
print(re.findall(pattern, my_string))  


##### email validation #####

email = "alberto.ramirez@uc.edu.py"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"  # Esta
                                            # expresion de validacion 
                                            # necesita ser mejorada
                                            # !!!!!!!!!!!!
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))


email = "alberto.ramirez@uc" # Retorna lista vacia.
                             # Email no valido
print(re.findall(pattern, email))


email = "alberto.ramirez@uc." # Retorna lista vacia.
                              # Email no valido
print(re.findall(pattern, email))


email = "alberto.ramirezuc.edu.py" # Retorna lista vacia.
                                   # Email no valido
print(re.findall(pattern, email))


email = "alberto.ramirez@uc.edu.py" # Retorna lista vacia.
                                     # Email no valido
print(re.findall(pattern, email))


################################################
# Para aprender y alidar Expresiones Regulares:
# https://regex101.com/
################################################




 
 







                       

                      
                                                        