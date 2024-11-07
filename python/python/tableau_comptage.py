tab = [11,20,11,25,14,14,11]
ele = int(input("entrez un nombre"))
compte = 0
for nombre in tab:
    if nombre == ele:
        compte += 1
print(f"L'élément {ele} apparaît {compte} fois dans le tableau.")