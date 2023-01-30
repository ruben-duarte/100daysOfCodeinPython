char = input("Enter a char:  ")[0]
print(char)

result = eval(input("Enter an expression: "))
print(result)

if True:
    print("Hey")

if False:
    print("bye")

x = 3
r = x % 0

if r == 0:
    print(" Even ")
    if x > 7:
        print(" Bigger than 7")
    else:
        print(" Smaller than 7")
else:
    print("odd ")


if x == 1:
    print("One")
elif x == 2:
    print("Two")
elif x == 3:
    print("Three")
else:
    print(" bigger than Four")

