import random


def adivina_el_numero(x):

    print("="*30)
    print("Bienvenido(a) al juego!")
    print("="*30)
    print(" Tu meta es adivinar el número generado por la computadora.")

    numero_aleatorio = random.randint(1, x)
    prediccion = 0
    while prediccion != numero_aleatorio:
        prediccion = int(input(f"Adivina un número entre 1 y {x} : "))

        if prediccion < numero_aleatorio:
            print("intenta de nuevo , este número es muy pequeño")
        elif prediccion > numero_aleatorio:
            print("intenta de nuevo , este número es muy grande.")
    print(f"felicitaciones! adivinaste el número { numero_aleatorio } correctamente")


adivina_el_numero(10)

