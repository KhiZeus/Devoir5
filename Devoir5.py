import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# index_col pour utiliser l'index fourni dans le fichier dans la premiere colonne
data_base = pd.read_csv('Census_2016_2021.csv',index_col=0)

# On selectionne les municipalités dans une nouvelle DataFramme reindexés
data_municipal = data_base[data_base['Type'] == 'MÉ'].reset_index(drop=True)
nombre_municipalites = len(data_municipal)
print(" le nombre de municipalités est: ", nombre_municipalites)

moyenne_2016 = round(data_municipal['Pop16'].mean(),0)
moyenne_2021 = round(data_municipal['Pop21'].mean(),0)
print("Lapopulation moyenne des municipalité est : \n"
     "Pour 2016 : ", moyenne_2016,"\n"
     "Pour 2021 : ", moyenne_2021)
data_municipal['accroissement_population'] = (data_municipal['Pop21'] - data_municipal['Pop16'])/data_municipal['Pop16']
print(data_municipal.head())

"""
print('\n')
print(data_municipal.head())
print('\n')"""