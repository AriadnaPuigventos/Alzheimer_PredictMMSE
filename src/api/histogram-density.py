import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def histogramdensity(): 
    adni = pd.read_csv("/Users/ariadnapuigventos/Documents/CURSOS/BRIDGE/DS_Ejercicios_Python/BootCamp_TheBridge/Alzheimers_Disease/Data/MCI_AD_CN_Final.csv", sep=",")
    sns.distplot(adni['MMSE Total Score'], hist_kws=dict(edgecolor="black", linewidth=1), color='Blue')
    fig.write_html('/templates/histogram.html')
