import numpy as np
tableau_1 = np.array([i for i in range(11)])
tableau_2 = np.array([i for i in range(30,41)])
#print(tableau_1)
#print(tableau_2)

print(f"tableau-1 = {tableau_1}")
print("tableau-2 = {0}".format(tableau_2))

print(type(tableau_1))

print (tableau_1 + 5)
print("tableau_modifié = {0}".format(tableau_1 + 5))

#Création d'un tableau unidimensionnel contenant les entiers de 0 à 9.
tableau_1 = np.array([i for i in range(11)])
# Création d'un tableau unidimensionnel contenant les entiers de 30 à 40.
tableau_2 = np.array([i for i in range(30,41)])

# a) Sélectionnez et imprimez les éléments pairs du premier tableau créé dans la partie a) de l'exercice 1.
# on applique un filtre (condition) sur tableau1
    #on cré une liste de filtre vide
liste_filtre = []
# on parcours les elements du array
for x in tableau_1 :
    if x % 2 == 0:
        liste_filtre.append(True)
    else :
        liste_filtre.append(False)

print(liste_filtre)

tableau_1_pair = tableau_1[liste_filtre]

print(tableau_1_pair)

print(type(tableau_1_pair))   