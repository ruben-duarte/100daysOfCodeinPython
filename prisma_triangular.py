import math

print("="*15)
print("Calculo del area perimetro y volumen de un prisma triangular")

lado = float(input("lado en cm: "))
altura = float(input("altura en cm: "))

area = round((lado)*((math.sqrt(3)*lado/2) +3*altura),2)
volumen = round(area*altura,2)

print(f"""
area superficial {area} cm2
volumen {volumen} cm3
""")