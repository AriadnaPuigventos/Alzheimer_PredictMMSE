import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def hypothesisscatter():
    adni = pd.read_csv("/Users/ariadnapuigventos/Documents/CURSOS/BRIDGE/DS_Ejercicios_Python/BootCamp_TheBridge/Alzheimers_Disease/Data/MCI_AD_CN_Final.csv", sep=",")
    adni['Visits_numbering'] = adni["Visit"].map({"ADNI1/GO Month 12":4, "ADNI1/GO Month 24":6,'ADNI2 Year 1 Visit':6.5,'ADNI2 Year 2 Visit':7,'ADNI2 Year 3 Visit':8,'ADNI2 Year 4 Visit':9})
    adni.plot.scatter(x="Visits_numbering", y="MMSE Total Score", c="blue")
    fig.write_html('/templates/hyphotesis.html')