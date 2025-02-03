##CLASIFICACIÓN DE AÑOS
#SANTIAGO AGUILAR VESGA
#1097099391
def añoBisiesto(años):

    if (año % 4 == 0) and (año % 100 != 0) or (año % 400 == 0):
        print(f'El año {año} es bisiesto')
    else:
        print(f'El año {año} es común')

año = int(input("Ingrese un año: "))
determinar = añoBisiesto(año)
