nombres = [
    ["Adrián"],
    ["Alejandra"],
    ["Ámbar", "Isabella"],
    ["Andrés", "David"],
    ["Aura", "Camila"],
    ["Camilo", "Andrés"],
    ["Daniel", "Esteban"],
    ["David", "Santiago"],
    ["Edgar", "Leonardo"],
    ["Gerson", "Steven"],
    ["Harley", "Yefrey"],
    ["John", "Stiven"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "Eduardo"],
    ["Juan", "Fernando"],
    ["Juan", "Jose"],
    ["Maria", "Juliana"],
    ["Mateo", "Roman"],
    ["Naya", "Zarela"],
    ["Nicolas"],
    ["Omar", "Fernando"],
    ["Santiago"],
    ["Santiago", "Andrés"],
    ["Santiago"],
    ["Sara", "Sofía"],
    ["Sayara", "Yurley"],
    ["Sergio", "Andrés"],
    ["Simón", "Dante"],
    ["Thomas", "Sebastián"],
    ["Vladimir"]
]

apellidos = [
    ["Quintero", "Pinzón"],
    ["Pinzón", "Alvarez"],
    ["Plata", "López"],
    ["Reyes", "Espinel"],
    ["Pico", "Araque"],
    ["Suárez", "Fuentes"],
    ["Guerrero", "Quintero"],
    ["Vera", "Mendez"],
    ["Acevedo", "Arteaga"],
    ["Chaparro", "Martínez"],
    ["Cabrales", "Vargas"],
    ["Negron", "Regalado"],
    ["Saavedra", "Jaimez"],
    ["Santoyo", "Jaimes"],
    ["Vargas", "Soto"],
    ["Pinilla", "Guzmán"],
    ["Umaña", "Barragan"],
    ["Abril", "Roman"],
    ["Saavedra", "Mejia"],
    ["Camargo"],
    ["Lizcano", "Jaimes"],
    ["Chedraui", "Mantilla"],
    ["Granados", "Parra"],
    ["Aguilar", "Vesga"],
    ["Quiñonez", "Sosa"],
    ["Jaimes", "Perez"],
    ["Díaz", "Rodríguez"],
    ["Aparicio", "Arciniegas"],
    ["Rueda", "Hernández"],
    ["Salamanca", "Galvis"],
    ["Bastos", "Garcia"],
    ["Diaz", "Contreras"]
]
booleanito=True
while booleanito == True:
    print ("""
    1. Ver estudiantes
    2. Agregar estudiantes
    3. Editar estudiantes
    4. Eliminar estudiantes
    5. Salir
    """)
    user = int((input("Bienvenido al programa, seleccione una opción: ")))
    if user == 2: 
        ## AGREGAR ESTUDIANTES
        PrimerNombre = input("Ingrese el primer nombre: ")
        SegundoNombre = input("Ingrese el segundo nombre: ")
        ListaNombres = [PrimerNombre, SegundoNombre]
        nombres.append(ListaNombres)
        Apellido1 = input("Ingrese el primer apellido: ") 
        Apellido2 = input("Ingrese el segundo apellido: ")
        ListaApellidos = [Apellido1, Apellido2]
        apellidos.append(ListaApellidos)
        for i in range (len(nombres)):
            NombresCompletos = " ".join(nombres[i]) + " " + " ".join(apellidos[i])
            print(f"Estudiante #{i+1}: {NombresCompletos}")
    elif user == 4:
        ##ELIMINAR ESTUDIANTES
        for i in range(len(nombres)):
            NombresCompletos = " ".join(nombres[i]) + " " + " ".join(apellidos[i])
            print(f"Estudiante #{i+1}: {NombresCompletos}")
        #############################################################
        EliminarEstudiante = int(input("¿Qué estudiante desea eliminar?: "))
        nombres.pop(EliminarEstudiante-1)
        apellidos.pop(EliminarEstudiante-1)
        print(f"Estudiante #{i+1}: {NombresCompletos}")
    ##EDITAR ESTUDIANTES
    elif user == 3:
        for i in range(len(nombres)):
            NombresCompletos = " ".join(nombres[i]) + " " + " ".join(apellidos[i])
            print(f"Estudiante #{i+1}: {NombresCompletos}")
        #############################################################
        EditarEstudiante = int(input("¿Cuál estudiante quieres editar?"))
        PrimerNombreNuevo = input("Primer nombre del estudiante: ")
        SegundoNombreNuevo = input("Segundo nombre del estudiante: ")
        NuevosNombres = [PrimerNombreNuevo, SegundoNombreNuevo]
        Apellido1Nuevo = input("Primer apellido del estudiante: ")
        Apellido2Nuevo = input("Segundo apellido del etudiante")
        NuevosApellidos = [Apellido1Nuevo, Apellido2Nuevo]
        nombres[EditarEstudiante-1]= NuevosNombres
        apellidos[EditarEstudiante-1]=NuevosApellidos

    elif user == 1:
        for i in range(len(nombres)):
            NombresCompletos = " ".join(nombres[i]) + " " + " ".join(apellidos[i])
            print(f"Estudiante #{i+1}: {NombresCompletos}")
    elif user == 5:
        booleanito = False
        break



    