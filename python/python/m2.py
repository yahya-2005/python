def cal_moyenne(tableau):
    if len(tableau) == 0:
        return 0 
    S = sum(tableau)
    M = S / len(tableau)
    return M  
tableau = [11, 15, 7, 19, 4, 17]
moyenne = cal_moyenne(tableau)
print("La moyenne des sommes du tableau est :", moyenne)