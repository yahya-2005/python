def comparer(x,y):
    if x > y : 
     print("la valeur de x est superieur à y")
    elif x < y : 
     print("la valeur de x est inferieur à y") 
    else : 
     print("la valeur de x et y sont égaux")   
#appel 
x = float(input("entrez la valeur de x :"))
y = float(input("entrez la valeur de y :"))
comparer(x,y)