## AGUILAR VESGA SANTIAGO
## 1097099391


##Solicitamos la entrada de datos al usuario
x = int(input("Ingrese la cantidad de terminos "))
print(x)
##Crear sumatoria para que inicialice en 0
sumatoria = 0
##Iniciamos el ciclo for en 1 hasta x(Numero ingresado por el usuario)
for i in range (1, x):
    if (i % 2 == 0): 
        sumatoria -= (1/i)
    else:
        sumatoria += (1/i)

print("El resultado de la sumatoria es: ", sumatoria)

## AGUILAR VESGA SANTIAGO
## 1097099391