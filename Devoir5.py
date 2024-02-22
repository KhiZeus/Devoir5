import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# index_col pour utiliser l'index fourni dans le fichier dans la premiere colonne
data_base = pd.read_csv('Census_2016_2021.csv',index_col=0)

# On selectionne les municipalités dans une nouvelle DataFramme reindexés
data_municipal = data_base[data_base['Type'] == 'MÉ'].reset_index(drop=True)
nombre_municipalites = len(data_municipal)
print(" le nombre de municipalités est: ", nombre_municipalites)

#Calcul et affichage des populations moyennes
moyenne_2016 = round(data_municipal['Pop16'].mean(),0)
moyenne_2021 = round(data_municipal['Pop21'].mean(),0)
print("Lapopulation moyenne des municipalité est : \n"
     "Pour 2016 : ", moyenne_2016,"\n"
     "Pour 2021 : ", moyenne_2021)
# Ajout d'une colonne acroissement en % dans la data frame
data_municipal['accroissement_population'] = 100*(data_municipal['Pop21'] - data_municipal['Pop16'])/data_municipal['Pop16']


#représentation des nuages de points représenatant le taux en foenction de la population de 2021
data_municipal.plot.scatter(x='Pop21', y='accroissement_population')
plt.xlabel("Population en 2021")
plt.ylabel("Taux d'accroissement de la population 2016-2021")
plt.title("Taux d'accroissement de la population en fonction de la population en 2021")
plt.savefig('accroissement_population.pdf')
plt.show(block=False)
plt.pause(3)
plt.close()
plt.clf()

#Classement dans cinq categorie C1,C2...C5
maxi_population21= max (data_municipal['Pop21'])
data_municipal['Population_Cat21'] = pd.cut(data_municipal['Pop21'], bins=[0, 1000, 2500, 5000, 10000, maxi_population21+1],\
                                          labels=['Moins de 1000', '1000 à 2499', '2500 à 4999', '5000 à 9999', 'plus de 10000'], right=False)
#compter le nombre de municipalités dans chaque categories
municipalite_par_categories21 = data_municipal['Population_Cat21'].value_counts()

#Représentation enbarre horizontale de la population dans chaque catégorie
municipalite_par_categories21.plot(kind='barh')
plt.xlabel("Nombre de municipalités")
plt.ylabel("Catégories de population")
plt.title("Répartition des municipalités selon la catégorie ")
plt.legend()
plt.savefig('municipalites_par_categories.pdf')
plt.pause(3)
plt.close()
plt.clf()


# BONUS
maxi_population16 = max(data_municipal['Pop16'])
data_municipal['Population_Cat16'] = pd.cut(data_municipal['Pop21'], bins=[0, 1000, 2500, 5000, 10000, maxi_population16+1],\
                                          labels=['Moins de 1000', '1000 à 2499', '2500 à 4999', '5000 à 9999', 'plus de 10000'], right=False)
#compter le nombre de municipalités dans chaque categories
municipalite_par_categories16 = data_municipal['Population_Cat16'].value_counts()


categories = list(municipalite_par_categories21.index)

bar_width = 0.25

x_pos = np.arange(len(categories))
bar21 = plt.bar(x_pos, municipalite_par_categories21, bar_width, label='2021')
bars16 = plt.bar(x_pos + bar_width, municipalite_par_categories16, bar_width, label='2016')
plt.xticks(x_pos + bar_width / 2, categories, rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.savefig('population_categories_comparatif.pdf')
plt.pause(3)
plt.close()
plt.clf()

