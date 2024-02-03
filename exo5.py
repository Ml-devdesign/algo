# Décompte
# Les variables retenues sont les suivantes : Nom, NbNom.
# Travail demandé
# Rédiger l’algorithme permettant de compter le nombre de noms saisis avant l’interruption de la
# saisie (lorsque l’on saisit « fin »)
# Vérification
# Écrire un algorithme qui demande un nombre compris entre 10 et 20, jusqu’à ce que la réponse
# convienne. En cas de réponse supérieure à 20, on fera apparaître un message : « Plus petit ! », et
# inversement, « Plus grand ! » si le nombre est inférieur à 10.
# Valeur
#-----------------------------------------------------------------------
nom=[]
stop=("fin")
nombrenom=int(input("Veuillez saisir un chiffre qui corespond au nombre d'entrer: "))


for i in range(nombrenom):
    saisie=input("veuillez saisire un nom ")
    nom.append(saisie)
    if saisie==stop:
        break
    print(nom)

for i in nombrenom:
    if nombrenom >= 20:
        print(f"{nombrenom}Plus petit !")
    elif nombrenom <= 10:
        print(f"{nombrenom} Plus grand ! ")
