def InteresSimple(Ci, i, t):
    """Funcion para calcular el interés simple"""
    InteresSimple = Ci * i * t
    return InteresSimple

def InteresCompuesto (Ci, i, t):
    """"Funcion para calcular el interés compuesto"""
    InteresCompuesto = Ci * (1 + i)**t
    return InteresCompuesto

def TotalGanado (i, Ci):
    """"Suma de interes simple/compuesto + Capital Inicial"""
    CapitalFinal = i + Ci
    return CapitalFinal

#Bienvenida al programa y preguntar qué funciones desea usar
print("Bienvenido al programa, a continuación se muestran las opciones")
print("Digite 1 ) Calcular Interés Simple")
print("Digite 2 ) Calcular Interés Compuesto")
usuario = int(input(" "))
if (usuario == 1):
    ##Solicitud de datos:
    solicitarCapitalInicial = float(input("Ingrese el Capital inicial: "))
    solicitartasaInteres = float(input("Ingrese la tasa de interés (%): "))
    solicitartasaInteres = solicitartasaInteres/100
    solicitarTiempo = float(input("Ingrese el tiempo en años: "))
    #Calcular resultados y mostrarlos en pantalla
    resultado = InteresSimple(solicitarCapitalInicial, solicitartasaInteres, solicitarTiempo)
    capitalfinal = float(TotalGanado(resultado, solicitarCapitalInicial))
    print("Después de ", solicitarTiempo, " año(s), obtendrás $", capitalfinal)
elif (usuario == 2):
    #Se solicitan resultados para caso 2
    solicitarCapitalInicial = float(input("Ingrese el Capital inicial: "))
    solicitartasaInteres = float(input("Ingrese la tasa de interés (%): "))
    solicitartasaInteres = solicitartasaInteres/100
    solicitarTiempo = float(input("Ingrese el periodo de ahorro: "))
    # Calcular resultados
    resultado = InteresCompuesto(solicitarCapitalInicial, solicitartasaInteres, solicitarTiempo)
    capitalfinal = float(TotalGanado(resultado, solicitarCapitalInicial))
    print("Después de ", solicitarTiempo, " año(s), obtendrás $", capitalfinal)
else: 
    #Para asegurarse
    print("Has digitado incorrectamente")

#SANTIAGO AGUILAR VESGA
#1097099391



