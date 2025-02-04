## AGUILAR VESGA SANTIAGO
## 1097099391

##Solicitar la cantidad de empleados
N = int(input("Ingrese la cantidad de empleados"))
print(N)
mayorSueldo = 0
menorSueldo = 0
##Inicializar variables para evitar errores
totalBruto= 0 
totalEPS = 0 
totalPension = 0 
totalNeto = 0
nombreMayor = ""
nombreMenor = ""
##Ciclo for hasta n, que es la cantidad de usuarios a solicitar
for i in range (1, N):
    Nombre = input("Ingrese el nombre del empleado: ")
    print(Nombre)
    horas = int(input("Ingrese la cantidad de horas trabajadas"))
    print(horas)
    bruto = horas * 20000
    eps = bruto * 0.04
    pension = bruto * 0.04
    neto = bruto - eps - pension

    totalBruto = totalBruto + bruto
    totalEPS = totalEPS + eps
    totalPension = totalPension + pension
    totalNeto = totalNeto + neto

    if (neto>mayorSueldo):
        mayorSueldo = neto
        nombreMayor = Nombre
    
    if (neto <menorSueldo):
        menorSueldo = neto
        nombreMenor = Nombre
    
    print("Empleado ", Nombre)
    print("Sueldo Bruto $", bruto)
    print("Eps $", eps)
    print("Pension $", pension)
    print("Sueldo Neto $", neto)


promedioBruto = totalBruto/N
promedioNeto = totalNeto/N

print("Totales ")
print("Total Salarios Brutos: $", totalBruto)
print("Total EPS: $", totalEPS)
print("Total Pension: $", totalPension)
print("Total Salarios Netos: $", totalNeto)
print("Empleado que más gana: ", nombreMayor)
print("Empleado que menos gana: ", nombreMenor)

