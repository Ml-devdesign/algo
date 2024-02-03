# Exercice 1 :
# Rédiger un algorithme en pseudo-code qui demande à l’utilisateur de saisir le montant d’un produit acheté ainsi que la quantité acheté et qui affiche le montant totale avec une remise de 5 %.
#-----------------------------------------------------------------------
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
#-----------------------------------------------------------------------
# Exercice 3 :
# Saisissez le rayon R d’un cercle et un angle a (en degré(s)). Calculez et affichez l’aire du secteur circulaire.
# Aire = ∏ * R2 * a / 360
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# Partie III : Programmation Python
# Les Ours Brun
# La station de ski « Les ours bruns » a simplifié son système de tarification des forfaits de ski.
# Elle propose deux types de forfaits : à la journée ou à la saison.
# Le tarif varie en fonction du type de forfait et du statut du bénéficiaire qui dépend de son âge.
# Travail demandé
# À partir du document ci-après, on vous demande d’établir l’algorithme permettant de calculer et
# d’afficher le tarif unitaire du forfait demandé en précisant le statut du bénéficiaire.
# Vous utiliserez les variables suivantes : Statut, TypeForfait, Age, Tarif et vous attribuerez le chiffre 1
# au forfait à la journée et le chiffre 2 au forfait à la saison.
# Éléments de facturation : tarifs des forfaits
# Type de forfait Adultes Enfants - 12 ans Seniors > de 60 ans
# 1 journée 25,80 € 18,70 € 21,40 €
# Saison 510,00 € 300,00 € 340,00
#-----------------------------------------------------------------------
forfaitJournée1={"Adulte" : 25.80 ,"Enfants - 12" : 18.70 ,"Seniors" : 21.40}
forfaitSaison2={"Adulte":500.00 ,"Enfants - 12":300.00,"Seniors":340.00}

typeForfait={"forfait à la journée ":1,"forfait à la saison":2}
age=input("veuillez saisire votre Age : ")
saison=input("Veuillez saisir 1 pour au forfait à la journée et le chiffre 2 au forfait à la saison: ")

for i in age:

    if 12> age <60 and saison==1 :
        print(f"Tarif unitaire du {typeForfait[0]} : {forfaitJournée1[0]}")
    if age<12 and saison==1:
        print(f"Tarif unitaire du {typeForfait[0]} : {forfaitJournée1[1]}")
    if age <60 and saison==1:
        print(f"Tarif unitaire du {typeForfait[0]} : {forfaitJournée1[2]}")
    if 12> age <60 and saison==2 :
        print(f"Tarif unitaire du {typeForfait[1]} : {forfaitJournée1[0]}")
    if age<12 and saison==2:
        print(f"Tarif unitaire du {typeForfait[1]} : {forfaitJournée1[1]}")
    if age <60 and saison==2:
        print(f"Tarif unitaire du {typeForfait[1]} : {forfaitJournée1[2]}")

#-----------------------------------------------------------------------
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

    
#-----------------------------------------------------------------------
# Une voiture coûte 56 000 e et perd 7% de sa valeur chaque année.
# Rédiger le programme qui calcule et affiche la valeur de cette voiture au bout de 18 ans.
# BONUS : améliorer votre programme en demandant à l’utilisateur le prix d’achat de sa voiture et
# l’année à laquelle il souhaite la vendre. (Faire les vérifications nécessaires)
#-----------------------------------------------------------------------
voiture=56000
valeur=(voiture*7/100)
if valeur == valeur :
    value=voiture-valeur
print(f"Valeur de la voiture aprés 1 ans : {value}")
for value in range(18):


# voitureClient=int(input("Veuillez saisire le prix de votre voiture : "))
# anneeVente=int(input("Veuillez saisire l'année de vente :"))
#-----------------------------------------------------------------------