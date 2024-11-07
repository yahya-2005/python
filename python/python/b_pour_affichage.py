nombre = int(input("Entrez un nombre : "))

print(f"Les diviseurs de {nombre} sont :")
for i in range(1, nombre + 1):
    if nombre % i == 0:
        print(i)