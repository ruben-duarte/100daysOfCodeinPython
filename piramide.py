import math

print("="*10)
print("area superficial perimetro y volumen de piramide base cuadrada")

lado = float(input("Lado en cm: "))
altura = float(input("Altura en cm: "))

area = round( lado*(lado + math.sqrt(4*altura**2 + lado**2)),2)
volumen = round( (lado**2)*(altura)/3 ,2)
apotema = round(math.sqrt((lado/2)**2 + altura**2),2)
perimetro = round(4*lado + 4*apotema,2)

print(f"""
        area superficial {area} cm2
        volumen {volumen} cm3
        perimetro {perimetro} cm
        apotema {apotema} cm
        =================
        Gracias por utilizar nuestro programa

""")
