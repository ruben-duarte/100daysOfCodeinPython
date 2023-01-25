Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#atithmetic operators
x = 2
y = 3
x+y
5
x-y
-1
x*y
6
x/y
0.6666666666666666
#assigment operator
x = x + 2
x
4
x += 2
x
6
x *= 3
x
18
x/=6
x
3.0
a,b =5,6
a
5
b
6
#uniry operator
n = 7
n = -n
n
-7
#relational operator
a<b
True
a>b
False
a==b
False
a = 6
a==b
True
a<=b
True
a>=b
True
a!=b
False
b = 7
a!=b
True
#logical operators
a=5
b=4
a<8  and b<5
True
a<8 and b<2
False
a<8 or b<2
True
x = true
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    x = true
NameError: name 'true' is not defined. Did you mean: 'True'?
x = True
notx
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    notx
NameError: name 'notx' is not defined
not x
False
x
True
x = not x
