multiplos_3o5 = [ ]
n =1000

for k in range(n):
    if k%3==0 or k%5==0:
        multiplos_3o5.append(k)
suma = sum(multiplos_3o5)
print("+"*20)
print(f"la suma de los enteros multiplos de 3 y 5 abajo de 1000 es : {suma}")
print("+"*20)


#second method
suma =0
for z in range(1000):
    if z%3 == 0 or z%5 == 0 :
        suma += z

print("+"*20)
print(f"la suma de los enteros multiplos de 3 y 5 abajo de 1000 es : {suma}")
print("+"*20)

# references  
#https://plainmath.net/pre-algebra/20487-to-determine-the-sum-of-all-multiples-of-3-between-1-and-1000
#https://math.stackexchange.com/questions/9259/find-the-sum-of-all-the-multiples-of-3-or-5-below-1000