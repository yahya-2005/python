def calcul_air(L,l): 
    air = L*l 
    return air 
#appel 
L = float(input("entrez la longueur de rectangle :"))
l = float(input("entrez la largueur de rectangle :"))
print("air de retangle est : ",calcul_air(L,l))