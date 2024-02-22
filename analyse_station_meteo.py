import pandas as pd
import numpy as np


"""Ce script est une introduction a pandas
On peut voir le filtrage de champs
Essentiellement on analyse les noms des stations meteo"""

# On lit l'inventaire des stations meteo au Canada
download_url = (
    "https://collaboration.cmc.ec.gc.ca/cmc/climate/"
    "Get_More_Data_Plus_de_donnees/Station%20Inventory%20EN.csv"
)

# Le fichier est telecharge directement en memoire
inventory = pd.read_csv(download_url,skiprows=3)
print(inventory.head())

print('Liste des champs:\n',list(inventory.columns))

print('\n')
print('Nombre de station par province')
print(inventory.groupby('Province')['Name'].count())


# On cherche une station a MONTREAL qui fournit une info par heure de 1973 a 2023

# Recherche du mot cle MONTREAL au QUEBEC
df_montreal = inventory[inventory['Name'].str.contains("MONTREAL")*inventory['Province'].str.contains("QUEBEC")]

print('\n')
print('Nombre de stations a MONTREAL:',df_montreal['Name'].count())

print('\n')
print('Stations de MONTREAL mesurant par heure avant 1973')
df_select = df_montreal[df_montreal['HLY First Year'] <= 1973].loc[:,('Name','Climate ID','Station ID','HLY First Year','HLY Last Year')]
print(df_select)

print('\n')
print("Stations de MONTREAL mesurant par heure jusqu'en 2023")
df_select = df_montreal[df_montreal['HLY Last Year'] >= 2023].loc[:,('Name','Climate ID','Station ID','HLY First Year','HLY Last Year')]
print(df_select)


