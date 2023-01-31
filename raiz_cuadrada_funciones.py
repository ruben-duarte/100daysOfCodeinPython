def enumeracion_exhaustiva( ):
    objetivo = int(input("Escoge un entero: "))
    respuesta = 0

    while respuesta**2 <objetivo:
        print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f"la raiz cuadrada de {objetivo} es {respuesta}")
    else:
        print(f" {objetivo} no tiene una raiz cuadrada exacta")


def aproximacion( ):
    objetivo = int(input("Escoge un número:"))
    epsilon = 0.001
    paso = epsilon**2
    respuesta = 0.0
    contador=0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
         print(abs(respuesta**2 - objetivo), respuesta,contador)
         respuesta += paso
         contador += 1

    if abs(respuesta**2 - objetivo) >= epsilon:
      print(f" No se encontro la raiz cuadrada {objetivo} ")
    else:
      print(f"La raiz cuadrada de {objetivo} es {respuesta}")


def escoger( ):
        print("="*15)
        opcion = int(input(" Escoge un metodo para la raiz cuadrada, '1' enumeracion exahustiva, '2' aproximacion "))
        print( )
        if opcion == 1:
            enumeracion_exhaustiva( )
        elif opcion == 2:
            aproximacion( )
        else:
            print("opcion incorrecta")

escoger( )