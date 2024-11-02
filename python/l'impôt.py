salaire = float(input("Entrez votre salaire : "))
if salaire < 20000:
    impot = 0
elif salaire <= 40000:
    impot = salaire * 0.1
else:
    impot = salaire * 0.2
print("L'impôt à payer est :", impot)
