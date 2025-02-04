## AGUILAR VESGA SANTIAGO
## 1097099391

##Algunas veces debemos definir las variables para evitar errores de indefiniciones
mayorNum = 0
menorNum = 0
##Creamos un ciclo para que se repita 10 veces
for i in range(1,11):
    print("Ingrese el termino #", i)
    n = int(input())
    print(n)
    if (mayorNum == 0) or (menorNum == 0):
        mayorNum = n
        menorNum = n
    else:
        if (n>mayorNum):
            mayorNum = n
        else:
            if (n<menorNum):
                menorNum = n
##Despues de realizar las comparaciones e ir almacenando datos, imprimimos los resultados
print("El numero mayor es: ", mayorNum)
print("El numero menor es: ", menorNum)

## AGUILAR VESGA SANTIAGO
## 1097099391