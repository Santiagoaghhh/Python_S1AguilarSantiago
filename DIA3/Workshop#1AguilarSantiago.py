def CelsiusToFarenheit(t):
    """Esta funcion convierte los grados Celcius a grados Farenheit"""
    conversion = (t * 9/5) + 32
    return conversion

def FarenheitToCelcius(t):
    """Esta funcion convierte los grados Farenheit a grados Celcius"""
    conversion = 5/9*(t - 32)
    return conversion

pregunta = input("Ingrese C para convertir a grados Celcius y F oara convertir a grados Farenheit ")
print(pregunta)
if (pregunta == "F"):
    solicitarTemperatura = float(input("Ingrese la temperatura en grados Celcius: "))
    print(solicitarTemperatura)
    resultado = CelsiusToFarenheit(solicitarTemperatura)
    print("La temperatura en grados Farenheit es: ", resultado)
elif (pregunta == "C"):
    solicitarTemperatura = float(input("Ingrese la temperatura en grados Farenheit: "))
    print(solicitarTemperatura)
    resultado = FarenheitToCelcius(solicitarTemperatura)
    print("La temperatura en grados Celcius es: ", resultado)
else:
    print("Has ingresado mal la letra")


#SANTIAGO AGUILAR VESGA
#1097099391