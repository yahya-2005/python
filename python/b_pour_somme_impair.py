n = int(input("Entrez un nombre entier : "))
somme_impairs = 0
for i in range(1, n + 1):
    if i % 2 != 0: 
        somme_impairs += i
print(f"La somme des nombres impairs entre 1 et {n} est : {somme_impairs}")