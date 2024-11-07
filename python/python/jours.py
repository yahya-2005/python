mois = int(input("Entrez un numéro de mois (1 à 12) : "))
if mois in [1, 3, 5, 7, 8, 10, 12]:
    jours = 31
elif mois in [4, 6, 9, 11]:
    jours = 30
elif mois == 2:
    annee = int(input("Entrez une année : "))
    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        jours = 29
    else:
        jours = 28
else:
    jours = "invalide"
print("Le nombre de jours dans le mois est :", jours)