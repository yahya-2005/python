def factorielle(n):
    if n == 0 or n == 1 :
        return 1 
    else : 
        return n * factorielle(n - 1)
# appel 
n = int(input("entrez la valeur de n :"))
R = factorielle(n)
print("le factorielle de n est :",R)