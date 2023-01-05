n = int(input("Enter an integer number "))

if n % 2 != 0:
    print('Blue')
elif n % 2 == 0 and range(2,6):
    print('not blue')
elif n % 2 == 0 and range(6,21):
    print('Blue')
elif  n % 2 == 0 and n >20:
     print('not blue')


if n % 2 != 0:
    print("Weird")
else:
    if 1 < n <= 5:
        print("Not Weird")
    elif 5 < n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")