'''
This module are for function to open and read files
'''

import json #Instalado
import requests #Instalado
import pandas as pd #Instalado


def readcsv(ruta, sep):
      df = pd.read_csv(ruta, sep)
      return df

