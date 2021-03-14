'''
Date:201211
Functionally about collect, clean and wrangling methods data.
'''
import pandas as pd

#DATAFRAME 1 - 6 BEST MARATHONS MAJORS

def checkingdata():
    majors = pd.read_csv("/Users/ariadnapuigventos/Documents/CURSOS/BRIDGE/DS_Ejercicios_Python/BootCamp_TheBridge/Proyecto_Navidad_Ariadna/documentation/world_marathon_majors.csv", sep = ";")
    #It wants to check for the datatypes because there is a time column, that maybe It had to change it to int.
    table_check = majors.dtypes
    print(table_check)

majors = pd.read_csv("/Users/ariadnapuigventos/Documents/CURSOS/BRIDGE/DS_Ejercicios_Python/BootCamp_TheBridge/Proyecto_Navidad_Ariadna/documentation/world_marathon_majors.csv", sep = ";")

def topandtail():
    #To display the top 10 in the best marathon majors in the over the world and the last 5 in the ranking.
    bestones = majors.head(10)
    print(bestones)
    print("......")
    lastones = majors.tail(5)
    print(lastones)

def dimention():
    #To knows how many columns and rows and if there are some duplicates rows.
    dimention_table = majors.shape
    print(dimention_table)
    mostrardeduplicados = majors[majors.duplicated()]
    print("number of duplicate rows: ", mostrardeduplicados)
    majorsOK = majors.drop_duplicates()
    print(majorsOK)
    print(majorsOK.shape)

def repite_pais():
    #To knows if there are some country who has won more than one time the same marathon or different.
    nacionalidad = majors.country.value_counts().head(15)
    print(nacionalidad)

def repetidores():
    #To knows if there are some winners who has won more than one time the same marathon or different.
    repetidores = majors.winner.value_counts().head(15)
    print(repetidores)

def changetype():
    #This function pretends to changes time column in major dataframe to timedelta to sum() in the future.
    time_column = pd.to_timedelta(majors["time"].str.strip())
    print(time_column)
    in_seconds = time_column.astype('timedelta64[s]')
    print(in_seconds)


#DATAFRAME 2 - ALTITUDE BY COUNTRIES

df = pd.read_csv("/Users/ariadnapuigventos/Documents/CURSOS/BRIDGE/DS_Ejercicios_Python/BootCamp_TheBridge/Proyecto_Navidad_Ariadna/documentation/altitud_countries.csv", sep= ";")

def droppingcolumns():
    df = pd.read_csv("/Users/ariadnapuigventos/Documents/CURSOS/BRIDGE/DS_Ejercicios_Python/BootCamp_TheBridge/Proyecto_Navidad_Ariadna/documentation/altitud_countries.csv", sep= ";")
    altitude = df.drop(["country", "Unnamed: 4", "Unnamed: 5", "Unnamed: 6"], axis=1).rename(columns={"name": "country"})
    print(altitude)

# DATAFRAME TIME SPENT HOURS

dict2 = {"Tasks": ["Searching datasets", "Path control", "Working in modules: functions, bucles...", "Wrangling Data: NaN, duplicates, outliers", "Visualization Data: graphics, boxplots", "Analyzing results", "Researching for value added"], "Hours": [32, 15, 72, 24, 192, 24, 12]}
Tasks = pd.DataFrame(dict2)