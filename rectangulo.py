import math


print("="*15)
print("Area,diagonal y  perímetro de un rectangulo")
print( )

base = float(input( "Base en cm:  "))
altura = float(input( "Altura en cm: "))

area = round(base * altura,2)
perimetro = round((base + altura)*2,2)
diagonal = round(math.sqrt(base**2 + altura**2),2)

print("="*15)
print(f"El área del rectangulo es {area}  cm2")
print(f"El perimetro del rectangulo es {perimetro} cm")
print(f"la diagonal del rectangulo es {diagonal} cm")
print("="*15)