##SANTIAGO AGUILAR
n1 = int(input("Ingresa el primer numero "))
print(n1)
n2 = int(input("Ingresa el segundo numero "))
print(n2)
suma1 = 0
suma2 = 0

##Crear ciclos for que evaluen los divisores y se vayan sumando
for i in range(n1):
    if (n1 % i == 0):
        suma1 = suma1 + i

for i in range(n2):
    if(n2 % i == 0):
        suma2 = suma2 + i
##Crear condicionales que impriman en base a los resultados
if (suma1 == n2) and (suma2 == n1):
    print (n1, " y ", n2, "son numeros amigos")
else: 
    print (n1, " y ", n2, "no son numeros amigos")
##SANTIAGO AGUILAR VESGA