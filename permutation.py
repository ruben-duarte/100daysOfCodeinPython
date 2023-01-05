#permutation of xxx  where x can be (0,9)
a= 0
b = 0
c = 0

for left_digit in range(10):
    a +=1
    for middle_digit in range(10):
        b += 1
        for right_digit in range(10):
            c +=1
            print(f"{left_digit}:{middle_digit}:{right_digit}")

permutation = a * b 
print("El numero de permutaciones es: ", permutation)
            

