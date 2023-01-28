import random


def jugar( ):
    usuario = input("Escoge una opción :  'pi'  para piedra, 'pa' papel, 'ti' tijera. \n").lower( )
    computadora = random.choice(['pi','pa','ti'])

    if usuario == computadora:
        return f'Empate! la computadora escogió {computadora}'

    if gano_el_jugador(usuario, computadora):
        return f' Ganaste! la computadora escogió {computadora}'

    return f'perdiste! la computadora escogió {computadora}'


def gano_el_jugador(jugador, oponente):
    if ((jugador == 'pi' and oponente == 'ti' )
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False


print(jugar( ))
