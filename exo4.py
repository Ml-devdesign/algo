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