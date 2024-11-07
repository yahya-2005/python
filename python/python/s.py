s = 0 
for i in range(8):
    print("entrez un nombre",i+1,":")
    n = int(input())
    if n < 0 : 
        continue
    s = s + n 
print("la somme des nombres est : ", s)