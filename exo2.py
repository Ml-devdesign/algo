# Exercice 2 :
# Rédiger un algorithme qui, à partir d’une année de naissance, calcule l’âge et affiche le résultat à l’utilisateur.
# On considère que la fonction ANNEE() nous donne l’année en cours.
#-----------------------------------------------------------------------
age=int(input("Annee de naissance: "))
anneeactu=2023 
for age in anneeactu:
    if age>0:
        i=anneeactu-age
    print(f"Votre age est de : {i}")