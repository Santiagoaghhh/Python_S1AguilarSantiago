##Check if a number is even or odd
def ParOImpar(n):
    ##Esta funcion revisará si el número es Par o Impar y retornará TRUE/FALSE
    if n % 2 == 0:
        n = True
        return n
    else: 
        n = False
        return n

n = int(input("Digite un número: "))
checkeo = ParOImpar(n)
if checkeo:
    print("El número ", n, " es par")
else:
    print("El número ", n, " es impar")

#Números Primos o Compuestos

def primos(x):
    if (x>2):
        for i in range (2, n):
            if (x % i == 0):
                return False
            else:
                return True

x = int(input("Ingrese un número: "))
primos(x)
if x == False:
    print("El número ", x, " es compuesto")
else: 
    print("El número ", x, "es primo")


## Raíz perfecta
import math
def raiz(r):
    e = math.sqrt(r)
    if e % 1 == 0:
        return True


r = int(input("Ingrese un número: "))
Raiz = raiz(r)
if Raiz:
    print("El número ", r, "es una raíz perfecta")
else:
    print("El número ", r, " no es una raíz perfecta")

##SANTIAGO AGUILAR VESGA
#1097099391