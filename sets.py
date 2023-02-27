set_countries = {'col', 'mex','Bol'}
print(set_countries)

set_numbers = {2,2,3,4}
print(set_numbers)

set_types = {1, False, 'hi'}
print(set_types)

#set desde un string
set_from_string = set('holaa')
print(set_from_string)

set_from_tuples = set(('abc', 'xyz', 'abz', 'xyz'))
print(set_from_tuples)

numbers = [1,2,3,3,5,0]
set_numbers = set(numbers)
print(set_numbers)

unique_numbers = list(set_numbers)
print(unique_numbers)

# Crud en sets

set_countries = {'col', 'jpn','bra'}
size = len(set_countries)
print('col' in set_countries)

#añadir
set_countries.add('pe')
print(set_countries)

#update
set_countries.update({'arg', 'ecu'})
print(set_countries)

#remove
set_countries.remove({'arg'})
print(set_countries)

set_countries.remove({'usa'})
set_countries.discard('usa')
print(set_countries)

set_countries.clear()

"""
add(): Añade un elemento.

update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.

discard(): Elimina un elemento y si ya existe no lanza ningún error.

remove(): Elimina un elemento y si este no existe lanza el error “keyError”.

pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.

clear(): Elimina todo el contenido del conjunto.

"""

#operations sets

set_a = {'col', 'mex','bol'}
set_b = {'pe', 'bol'}

set_c = set_a.union(set_b)
set_d = set_a | set_b

set_c = set_a.intersection(set_b)
set_c = set_a & set_b

set_c = set_a.difference(set_b)
set_c = set_a - set_b

set_c = set_a.symmetric_difference(set_b)
set_c = set_a ^ set_b


"""
    Operaciones set

union(set): Realiza la operacion “union” entre dos conjuntos. La unión entre dos conjuntos es sumar los elementos de estos sin repetir elementos. Esta operación tambien se puede realizar con el signo “|”: set_a | set_b.
intersection(set): Realiza la operacion “intersection” entre dos conjuntos. La intersección entre dos conjuntos es tomar unicamente los elementos en común de los conjutnos. Esta operación tambien se puede realizar con el signo “&”: set_a & set_b.
difference(set): Realiza la operacion “difference” entre dos conjuntos. La diferencia entre dos conjuntos es restar los elementos del segundo conjunto al primero. Esta operación tambien se puede realizar con el signo “-”: set_a - set_b.
symmetric_difference(set): Realiza la operacion “symmetric_difference” entre dos conjuntos. La diferencia simetrica entre dos conjutnos consta de restar todos los elementos de ambos exceptuando el elemento en común. Esta operación tambien se puede realizar con el signo “^”: set_a ^ set_b.
NOTA: No se pueden realizar operaciones con otras colecciones de datos, solo se puede únicamente entre conjuntos.

"""

