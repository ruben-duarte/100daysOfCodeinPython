import math

print("="*10)
print("area superficial perimetro y volumen de un cono ")

PI = 3.1415
radio = float(input("Radio en cm: "))
altura = float(input("Altura en cm: "))

generatriz = math.sqrt(altura**2 + radio**2)
area = round(PI*radio*(radio + generatriz),2)
perimetro = round(2*PI*radio,2)
volumen = round((PI*altura*radio**2)/3,2)

print("="*10)
print(f"""
area superficial : {area} cm2
perimetro : {perimetro} cm
volumen : {volumen} cm3
""")
print( )
print("="*10)



