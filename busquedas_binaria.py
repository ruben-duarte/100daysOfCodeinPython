import random
import time


def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# mi_lista = [1,3,5,10,12]
# print(busqueda_ingenua(mi_lista, 10))

def busqueda_binaria(lista, objetivo, limite_inferior = None, limite_superior = None):
    if limite_inferior is None:
        limite_inferior = 0
    if limite_superior is None:
        limite_superior = len(lista) - 1
    if limite_superior < limite_inferior:
        return -1
    
    punto_medio = (limite_inferior + limite_superior)//2

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferior, punto_medio -1)
    else:
        return busqueda_binaria(lista, objetivo, punto_medio +1 , limite_superior)
    

if __name__ == '__main__':
        # mi_lista = [1,3,5,10,12]
        # print(busqueda_binaria(mi_lista, 12))
        tamano = 10000
        conjunto_inicial = set()

        while len(conjunto_inicial) < tamano:
            conjunto_inicial.add(random.randint(-3*tamano, 3*tamano))

        lista = sorted(list(conjunto_inicial))
        # medir tiempo
        inicio = time.time()
        for objetivo in lista:
            busqueda_ingenua(lista, objetivo)
        fin = time.time()

        print(f"tiempo de busqueda ingenua:  {fin - inicio} segundos")

        inicio = time.time()
        for objetivo in lista:
            busqueda_binaria(lista, objetivo)
        fin = time.time()

        print(f"tiempo de busqueda binaria: {fin - inicio} segundos")
    

