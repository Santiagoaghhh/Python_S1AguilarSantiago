print("1. Millas a Kilómetros ")
print("2. Celcius a Farenheit")
print("3. Kilogramos a libras ")
usuario = int(input("Ingrese la funcion que quiera usar: "))
def MaKm(m):
    MaKm = m * 1.6093445
    return MaKm
    
def CelsiusToFarenheit(c):
    """Esta funcion convierte los grados Celcius a grados Farenheit"""
    conversion = (c * 9/5) + 32
    return conversion

def Ktolb(kg):
    lb = kg * 2.204
    return lb


match usuario:
    case 1:
        m = float(input("Ingrese las millas: "))
        conversion = MaKm(m)
        print(m, " millas son ", conversion, " en kilómetros")
    case 2:
        c = float(input("Ingrese la temperatura en grados Celcius"))
        temperaturaF = CelsiusToFarenheit(c)
        print("Temperatura: ", temperaturaF)
    case 3:
        kg = float(input("Ingrese los kg: "))
        lb = Ktolb(kg)
        print(lb, "lb ")

#SANTIAGO AGUILAR VESGA
#1097099391