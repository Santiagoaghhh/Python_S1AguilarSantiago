#SANTIAGO AGUILAR VESGA
#1097099391

PreguntarClima = input("""" INDICA COMO ES EL CLIMA:
                       soleado, lluvioso o frío
                       """)
minus = PreguntarClima.lower()

PreguntarHora = input("""" INDICA LA HORA:
                       mañana, tarde o noche
                       """)

minush = PreguntarClima.lower()

if minush == "mañana":
    match minus:
        case "soleado":
            print("Toma un buen jugo y ensalada")
        case "lluvioso":
            print("Desayuna un tamal con un buen café")
        case "frío":
            print("Deberías tomar chocolate Caliente")
        case _:
            print("Error, escribiste mal el clima, revisa de nuevo ;)")
elif minush == "tarde":
    match minus:
        case "soleado":
            print("Toma un buen jugo con un plato de proteínas y carbohidratos ")
        case "lluvioso":
            print("Te vendría bien un Mute")
        case "frío":
            print("Tal vez un pollo asado y sopa de arroz te reconforten")
        case _:
            print("Error, escribiste mal el clima, revisa de nuevo ;)")
elif minush == "noche":
    match minus:
        case "soleado":
            print("Hace calor, tal vez unas buenas bebidas frías ayuden")
        case "lluvioso":
            print("A nadie le hace mal un té para no comer pesado")
        case "frío":
            print("Deberías tomar chocolate caliente con un croasán")
        case _:
            print("Error, escribiste mal el clima, revisa de nuevo ;)")
