def parite(n):
    if n % 2 == 0 :
        return print("Le nombre ", n, " est pair.")
    else :
        return print("Le nombre ", n, " est impair.")
#appel 
n = int(input("entrez la valeur du nombre n :"))
resultat = parite(n)
print(resultat) 