#lists
my_list = list("Hola mundo")
print(my_list)
my_list[4] = []
print(my_list)
my_list.pop(4)
print(my_list)
my_list[1:1] = [0,0,0]
print(my_list)
numbers = [1,2,3,4]
numbers[1:1] = []
print(numbers)
numbers[1:1] = [7,8]
print(numbers)
numbers[1:1] = [ ]
print(numbers)


#range
print(range(7))
for i in range(1,7):
    print(i * 'O')

#range(1:7:2)   start, stop , step

print(range(1,7,2))
for i in range(1,7,2):
    print(i * 'O')

print(range(1,7,3))
for i in range(1,7,3):
    print(i * 'O')

print(range(1,7,-2))
for i in range(1,7,-2):
    print(i * 'O')



#sum numbers from 1 to 100

suma = sum(range(1,101))
print(suma)

n = 100
suma = n * (n+1) / 2
print(suma)