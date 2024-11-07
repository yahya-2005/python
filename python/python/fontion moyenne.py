def moyenne(liste):
    if len(liste) == 0:
        print("La liste est vide, aucune moyenne à calculer.")
        return
    somme = sum(liste)
    moyenne_valeur = somme / len(liste)
    print("La moyenne des nombres est :", moyenne_valeur)
n = int(input("Entrez le nombre d'éléments dans la liste : "))
liste = []
for i in range(n):
    nombre = float(input(f"Entrez le nombre {i + 1} : "))
    liste.append(nombre)
moyenne(liste)
