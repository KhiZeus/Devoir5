import pandas as pd
import numpy as np

"""
Ce script lit les donnees de statistiques canada 
de population des recensements 2021 et 2016
ainsi que la superficie des territoire recenses
et nettoye les donnees pour faciliter les analyses !
"""

# Base de donnees issue de Statistiques Canada
# Tableau 98-10-0002-02  Chiffres de population et des logements : Canada, provinces et territoires, et subdivisions de recensement (municipalités)"
# https://www150.statcan.gc.ca/t1/tbl1/fr/tv.action?pid=9810000202
# En français sans les symboles pour le QUEBEC
# Pour les besoin du cours : 
# - Index multilignes modifies 
# - en-tete et pied de page supprimes 

# delimiter ";" et non virgules car en francais
# decimal "," virgule en francais et non point
# thousands " " espace en francais et non virgule
# usecols pour ne conserver que les valeurs pertinentes

df = pd.read_csv('9810000202-sanssymbole-mod.csv', delimiter=';', decimal=',', thousands=' ', usecols=(0, 1, 2, 3, 11))

print('Avant traitement, liste des colonnes:\n')
print(df.columns)
print('\n')

# # On ne conserve que les donnees de populatione et la superficie
# # Supression des colonnes non pertinentes
# cols = list(df.columns)
# cols_to_drop = cols[4:11] + cols[12:]
# df.drop(axis=1,columns=cols_to_drop,inplace=True)

print('Apres drop des colonnes qui ne nous intetessent pas, liste des colonnes:\n')
print(df.columns)
print('\n')

# On renomme pour manipuler
df.columns = ['Nom','Type','Pop21','Pop16','Km2']


print('Avec les nouveaux noms, liste des colonnes:\n')
print(df.columns)
print('\n')

print(df.head())

print('dtype des differentes colonnes\n')
for col in df.columns:
    print(col,df[col].dtype)
print('\n')

print('Conversion des colonnes de population\n')

# Les espaces delimites les milliers, on les enleve
for col in ['Pop21','Pop16']:
    df[col] = df[col].apply(lambda x: x.replace(' ',''))

# Les ".."  correspondent a des valeurs non fournies, on les remplace par des NaN
df = df.replace('..', np.nan)

# On convertit finalement en float
for col in ['Pop21','Pop16']:
    df[col] = df[col].astype(float)

print('dtype des differentes colonnes\n')
for col in df.columns:
    print(col,df[col].dtype)
print('\n')

print("Youpi c'est des donnees numeriques!!\n")

print(df.head())
print('\n')

print(df.describe())
print('\n')

# On sauvegarde pour ne plus souffrir :D
df.to_csv('Census_2016_2021.csv')
