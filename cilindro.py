import math

print("="*15)
print("Area superficial y volumen del cilindro")
print( )

altura = float(input("Altura en cm: "))
radio = float(input("Radio en cm: "))

PI = 3.1415
area_superficial = (2*PI*radio)*(radio + altura)
volumen = (PI*radio**2*altura)

print("="*15)
print(f"area superficial de {area_superficial} cm2")
print(f"volumen de {volumen} cm3")
print("="*15)