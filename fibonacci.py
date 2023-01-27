fibonacci = [1,2]
fibo_even = [ ]
suma = 0
index = 0

while suma< 4000000:
      fibo_next = fibonacci[index+1] + fibonacci[index] 
      fibonacci.append(fibo_next)
      index += 1
      suma = fibo_next


for k in range(len(fibonacci)):
    if  fibonacci[k] % 2 == 0:
        fibo_even.append(fibonacci[k])

suma_even = sum(fibo_even)

print(f" la suma de los numeros fibonacci  pares menores que 4 millones es de: {suma} ")