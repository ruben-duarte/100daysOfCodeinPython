import random

def  adivina_el_numero_computadora( x ):

        print("="*15)
        print("Bienvenido(a) al juego!")
        print("="*15)
        print(f"Selecciona un número entre 1 y {x} para que la computadora intente adivinar ")

        limite_inferior = 1
        limite_superior = x

        respuesta = " "
        while respuesta != "c":
            #Generar la prediccion
            if limite_inferior != limite_superior:
                prediccion = random.randint(limite_inferior, limite_superior)
            else:
                prediccion = limite_inferior
            #respuesta del usuario
            respuesta = input(f"Mi prediccion es {prediccion}. si es muy alta ingresa A, si es muy baja ingresa B. Si es correcta ingresa C. Digita aqui: ").lower( )

            if  respuesta == "a":
                limite_superior = prediccion -1
            elif respuesta == "b":
                limite_inferior = prediccion +1

        print(f"Si! la computdora adivino tu numero correctamente {prediccion}.")


adivina_el_numero_computadora(10)
