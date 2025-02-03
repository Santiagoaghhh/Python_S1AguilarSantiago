#SANTIAGO AGUILAR VESGA
#1097099391

ElegirMoneda = input("""Escoja la moneda a la que quiera cambiar
                1. EUROS
                2. Pesos
                3. Yenes
  """)
print(ElegirMoneda)

cantidad = input("Ingrese la cantidad de dolares a cambiar: ")

#match ElegirMoneda:
 #   case 1:
  #      cantidad = input("Ingrese la cantidad de dolares a cambiar: ")
   #     totalPesos = cantidad * 4100
    #    totalEuros = cantidad * 0.85
     #   totalYenes = cantidad * 110
      #  print(f"""{cantidad} dolares son:
       #     {totalPesos} pesos colombianos
        #    {totalEuros} euros
         #   {totalYenes} yenes""")

match ElegirMoneda:
    case 1:
        totalEuros = cantidad * 0.85
        print(f'{cantidad} dolares son {totalEuros} euros')
    case 2:
        totalPesos = cantidad * 4100
        print(f'{cantidad} dolares son {totalPesos} pesos colombianos')
    case 3:
        totalYenes = cantidad * 110
        print(f'{cantidad} dolares son {totalYenes} yenes')
    case _:
        print("Error, debiste haber digitado algo mal")