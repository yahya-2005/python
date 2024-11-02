a = int(input("Entrez le premier nombre entier positif (a) : "))
b = int(input("Entrez le deuxième nombre entier positif (b) : "))
produit = 0
compteur = 0
while compteur < b:
    produit += a  
    compteur += 1  
print(f"Le produit de {a} et {b} est : {produit}")
