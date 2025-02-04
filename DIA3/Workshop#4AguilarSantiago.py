#SANTIAGO AGUILAR VESGA
#1097099391
import random
##PASSWORD
def creador_aleatorio(n):
    caracteres = "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890_*?"
    password = random.sample(caracteres, n)
    passwordfinal = "".join(password)
    return passwordfinal

n = int(input("Ingrese de cuantos carácteres va a ser su contraseña: "))
contrasena = creador_aleatorio(n)
print(f'Su contraseña de {n} caracteres es: {contrasena}')

