def singne(a,b) :
    if a * b > 0 : 
        print("les deux nombre est de meme signe")
    else :
        print("les deux nombre est de signe different")
def max(a,b) :
    if a > b : 
        return a    
    else: 
        return b 
def min(a,b) :
    if a < b : 
        return a 
    else : 
        return b 
# appel 
a = int(input("entrez la valeur de a :"))
b = int(input("entrez la valeur de b :"))
singne(a,b)
print("la valeur max entre a et b est : " ,max(a,b))
c = min(a,b) 
print("la valeur min entre a et b est : ", c)