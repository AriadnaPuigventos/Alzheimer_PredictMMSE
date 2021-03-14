'''
Date:201211
Funciones generales y varios para diferentes temáticas.
'''
import pandas as pd
import numpy as np
import os
import sys

#Función para mostrar todos los atributos que tiene una clase.
class whatwever:
     def print_instance_attributes(self):
        """Función para ver todos los atributos con sus valores"""
        for attribute, value in self.__dict__.items():
            print(attribute, '=', value)
            pass
"--------------------"   

#Función de PATH para ascender de niveles en la ruta madre:
def get_root_path(n):
    path = os.getcwd()
    for i in range(n): #números de niveles de la ruta hasta llegar a la raíz (código fuente) sin contar la carpeta madre.
      print(path)
    path = os.path.dirname(path)
    sys.path.append(path)
get_root_path(n=#numeros de niveles)
pass

"--------------------"

#Función para ordernar descendente:
top = df.groupby('column').sum()
top = df.sort_values(["column"], ascending=False)
pass

"""WIP"""

filter(lambda item: item[] expression, iterable)
#EJemplo: https://www.digitalocean.com/community/tutorials/how-to-use-the-python-filter-function-es#:~:text=Usar%20filter()%20con%20una,False%20%2C%20se%20suelta%20el%20valor.
lista = ['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie']


def names_vowels(x):
  return x[0].lower() in 'aeiou'

filtered_names = filter(names_vowels, creature_names)

print(list(filtered_names))
pass