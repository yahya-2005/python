def CelsiusEnFahrenheit(Tc):
    TF = (Tc * 9 / 5) + 32 
    return TF 
# appel 
Tc = float(input("entrez la valeur de degree celsius : ")) 
Tf = CelsiusEnFahrenheit(Tc) 
print("La température en Fahrenheit est :", Tf)