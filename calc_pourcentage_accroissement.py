import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.dpi'] = 100
plt.rcParams['font.size'] = 14
plt.rcParams['figure.figsize'] = (12,6)

# Fichier preprocesse ! Voir preprocess_population_cours.py

# index_col pour utiliser l'index fourni dans le fichier dans la premiere colonne
df = pd.read_csv('Census_2016_2021.csv',index_col=0)


print(df.head())
print('\n')
print(df.describe())
print('\n')

# On selectionne uniquement les villes dans une nouvelle DataFramme avec un nouvel indice.
df_villes = df[df['Type'] == 'V'].reset_index(drop=True)



# Pourcentage d'accroissement : 100*(population de 2021 - population de 2016)/(population de 2016)
df_villes['PctAcc'] = 100 * (df_villes['Pop21'] - df_villes['Pop16'])/df_villes['Pop16']

# On classe avec ce champ > sort_values (classement par valeur)
df_villes_Acc = df_villes.sort_values('PctAcc',ascending=False)

print(df_villes_Acc)
# Humm pas très pertinent l'ile de Dorval ...

# On conserve uniquement les villes de plus de 5000 habitants
df_villes_Acc = df_villes_Acc[df_villes_Acc['Pop21'] > 5000]

print(df_villes_Acc)

# On peut faire un graphique en barres horizontales
# Ici seulement les 15 premieres villes de classement grace a la fonction iloc
df_villes_Acc.iloc[:15,:].plot(kind='barh',y='PctAcc',x='Nom')
plt.xlabel('Accroissement de la population de 2016 a 2021 [%]')
plt.ylabel('Villes de plus de 5000 habitants')
plt.show()
