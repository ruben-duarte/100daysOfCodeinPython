print("="*15)
print("WELCOME!")
print("="*15)
print( )
print("="*15)
nombre1 = input("Ingresa tu nombre ")
edad1 = int(input("Ingresa tu edad "))
nombre2 = input("Ingresa tu nombre ")
edad2 = int(input("Ingresa tu edad "))
print("="*15)

len_1 = len(nombre1)
len_2 = len(nombre2)

if edad1 >edad2:
    diferencia = edad1 - edad2
    print(f"{nombre1} es mayor que {nombre2}, {diferencia} años ; tu nombre {nombre1} tiene {len_1} letras")
    print(f"{nombre2} es menor que {nombre1} tiene {len_2} letras")
elif edad1 < edad2:
    diferencia = edad2 - edad1
    print(f"{nombre1} es menor que {nombre2}, {diferencia} años,  tu nombre {nombre1} tiene {len_1} letras")
    print(f"{nombre2} es mayor que {nombre1} tiene {len_2} letras")
else:
    print(f"{nombre2} tiene la misma edad que {nombre1}")

print("="*15)

