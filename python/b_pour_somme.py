n = int(input("Entrez un nombre entier : "))
somme_cubes = 0
for i in range(1, n + 1):
    somme_cubes += i ** 3

print(f"La somme des cubes des nombres de 1 à {n} est : {somme_cubes}")
