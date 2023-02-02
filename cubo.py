import math

print("="*15)
print("Area superficial perimetro y volumen del cubo")
print( )

lado = float(input("Lado en cm: "))

area_cubo = 6*lado**2
volumen = lado**3
perimetro = lado*12

print("="*15)
print(f"Area es de {area_cubo} cm2 \nvolumen de {volumen} cm3 \nperimetro de {perimetro} cm")
print("="*15)