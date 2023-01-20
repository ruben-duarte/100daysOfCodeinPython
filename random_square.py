import random
lado = int(input("Lado del cuadrado en cm: "))
for k in range(lado):
    print("*"*lado)
print( )
print("*"*20)
print("cuadrado aleatorio")
lado_random = random.randint(1,50)
for h in range(lado_random):
    print("*"*lado_random)

print("*"*20)
print("triangulo aleatorio")
for m in range(lado_random):
    print("*"*m)
 
