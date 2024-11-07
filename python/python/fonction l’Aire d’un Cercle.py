def air_cercle(R) :
    air = 3.14 * R * R
    return air
def  Perimetre_cercle(R):
    Perimetre = 2 * 3.14 * R
    return Perimetre
# appel 
R = float(input("entrez le rayon du cercle :"))
Perimetre = Perimetre_cercle(R)
air = air_cercle(R) 
print("Le périmètre du cercle est : ", Perimetre)
print("L’aire du cercle est : ", air)