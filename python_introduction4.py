Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#data types
#none
none
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    none
NameError: name 'none' is not defined. Did you mean: 'None'?
None
a = None
b = none
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    b = none
NameError: name 'none' is not defined. Did you mean: 'None'?
type(None)
<class 'NoneType'>
# numeric
#int  float  complex  bool
num = 2.5
type(num)
<class 'float'>
num = 5
type(num)
<class 'int'>
num = 6 + 9j
type(num)
<class 'complex'>
a = 5.6
b = int(a)
type(b)
<class 'int'>
k = float(b)
type(k)
<class 'float'>
k
5.0
k = 6
c = complex(b,k)
c
(5+6j)
b < k
True
n = b < k
type(n)
<class 'bool'>
3=8
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
3==8
False
int(True)
1
int(False)
0
#sequence
#list tuple set string range
list = [23,44,55,44,33,5,6]
type(list)
<class 'list'>
s = {3,4,55,66,77,8}
type(s)
<class 'set'>
t = (2,3,4)
type(t)
<class 'tuple'>
string = "Rubens"
type(string)
<class 'str'>
st = 'a'
type(st)
<class 'str'>
range(0,10)
range(0, 10)
list(range(10))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    list(range(10))
TypeError: 'list' object is not callable
list(range(10))
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    list(range(10))
TypeError: 'list' object is not callable
list(range(1,5))
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    list(range(1,5))
TypeError: 'list' object is not callable
l1 = list(range(5))
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    l1 = list(range(5))
TypeError: 'list' object is not callable
list(range(2,10,2))
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    list(range(2,10,2))
TypeError: 'list' object is not callable
#dictionary
d = { 'ruben': 'samsung', 'raul':'nokia', 'carlos':'ericsson'}
d
{'ruben': 'samsung', 'raul': 'nokia', 'carlos': 'ericsson'}
d.keys()
dict_keys(['ruben', 'raul', 'carlos'])
d.values()
dict_values(['samsung', 'nokia', 'ericsson'])
d['ruben']
'samsung'
d['carlos']
'ericsson'
d.get('raul')
'nokia'
#lec 10