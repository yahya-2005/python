def operations(x,y):
    s = x + y
    pro = x * y 
    dif = x - y 
    if y != 0 : 
        quo = x / y 
        print("le quotient des deux nombre est :",quo)
    else: 
        print("error")
    print("la somme des deux nombre est :",s)
    print("la difference des deux nombre est :",dif)
    print("la produit des deux nombre est :",pro)
#appel 
a = float(input("entrez la valeur de a :" ))
b = float(input("entrez la valeur de b :" ))
operations(a,b) 