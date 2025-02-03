print("Binevenido a la calculador a de IMC")
peso=float(input("Ingrese su peso corporal en KG  "))
estatura = float(input("Ingrese su estatura en m: "))
def IMC(peso, estatura):
    IMC = peso / (estatura)**2
    return IMC

Indice = IMC(peso, estatura)


if IMC < 18.5:
    print("Bajo de peso")
elif IMC >= 18.5 and IMC <= 24.9:
    print("Peso normal")
elif IMC < 25 and IMC >= 29.9 :
    print("Sobrepeso")
elif IMC > 30 :
    print("Sobre peso")

#SANTIAGO AGUILAR VESGA
#1097099391