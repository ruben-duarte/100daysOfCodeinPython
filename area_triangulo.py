print(10*"+")
print("Area del triángulo")
base = float(input("base en cm  "))
altura = float(input("altura en cm "))
area = base*altura
print(f"El triángulo tiene un area de {area} cm2")
for i in range(int(altura)):
    for j in range(int(base)):
        print("+"*int(base))