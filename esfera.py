print("="*15)
print("area perimetro volumen esfera")

radio = float(input("radio en cm: "))

PI = 3.1415
area_superficial = round( 4*PI*radio**2,2)
volumen =round( (4*PI*radio**3)/3,2)
perimetro = round(2*PI*radio,2)

print(f"""
area superficial {area_superficial} cm2
volumen {volumen} cm3
perimetro {perimetro} cm
""")
print("="*15)