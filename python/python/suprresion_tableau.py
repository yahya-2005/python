tab = [11, 12, 5, 8, 20, 7, 11]
T1 = []
ele = int(input("Entrez un nombre : "))
for i in tab:
    if i != ele:
        T1.append(i)
print("Tableau après la suppression est :", T1)