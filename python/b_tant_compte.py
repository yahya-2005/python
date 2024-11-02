nombre = input("Entrez un nombre : ")
compteur = 0
while nombre:
    compteur += 1
    nombre = nombre[1:]  
print(f"Le nombre de chiffres est : {compteur}")
