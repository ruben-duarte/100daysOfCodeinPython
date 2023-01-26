Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
1+3
4
23
23
3 4.6
SyntaxError: invalid syntax. Perhaps you forgot a comma?
5/carro
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    5/carro
NameError: name 'carro' is not defined
7*"Hey"
'HeyHeyHeyHeyHeyHeyHey'
#print statement  salida
print('hey hola, mundo')
hey hola, mundo
#objeto  operador objeto
'hej' + 'vad heter du?'
'hejvad heter du?'
 a = 2
 
SyntaxError: unexpected indent
a=2
x=4
z = (a*x)/2
z
4.0
base = 2
altura = 4
area = (base*altura)/2
area
4.0
#reasignar variable
my_var = 'español'
my_var = 7
#string
my_string = 'English'
len(my_string)
7
my_string[0]
'E'
my_string[6]
'h'
# string name[comienzo: final:pasos]
my_string[ 2: ]
'glish'
my_string[  :3]
'Eng'
my_string[ :-2]
'Engli'
my_string[ :  : 2]
'Egih'
'I love ' + my_string
'I love English'
f' I love {my_string}'
' I love English'
f' I love {my_string}'*7
' I love English I love English I love English I love English I love English I love English I love English'
# entradas
nombre = input("cual es tu nombre?  ")
cual es tu nombre?  Ruben
print(' tu nombre es' , nombre)
 tu nombre es Ruben
print(f'tu nombre es{nombre}')
tu nombre esRuben
numero= int(input("Escribe un numero "))
Escribe un numero 4
numero
4
# operadores de comparacion  tests
3 == 3
True
7!=3
True
2<3
True
2>3
False
2<=3
True
#booleanos
True
True
Fals
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    Fals
NameError: name 'Fals' is not defined. Did you mean: 'False'?
False
False
not False
True
if 4>3:
    print("4 mayor que 3")

4 mayor que 3
# number system
bin(25)
'0b11001'
Ob0101
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    Ob0101
NameError: name 'Ob0101' is not defined
0b0101
5
0101
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
oct(25)
'0o31'
hex(25)
'0x19'
hex(10)
'0xa'
0xf
15
l=[31,52,65]
0b110011010
410
a=15
b=12
x = (a//4 + b**3) <2000 and (b%4 != 0)
x
False
a =5
b = 6
a = b
b = a
a
6
b
6
a =5
b=6
temp = a
a =b
b = temp
a
6
b
5
a =  a+b
b = a - b
a = a -b
a
5
b
6
#xor
a = a ^ b
b = a ^ b
a = a ^ b
a
6
b
5
a,b = b,a
a
5
b
6
x = 2 +4 +5
x = 2 +4 +5
#bitwise operators
#complement
~13
-14
~0
-1
~0
-1
~1
-2
12 & 13
12
12|13
13
25&24
24
12^13
1
10<<2
40
10>>2
2
