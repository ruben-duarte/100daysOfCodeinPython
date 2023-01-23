Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#tuple
tup = (34,56,78,98)
tup
(34, 56, 78, 98)
tup[1]
56
tup[1] = 33
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tup[1] = 33
TypeError: 'tuple' object does not support item assignment
s = {22,334,44,55,54,59}
s
{54, 55, 22, 59, 44, 334}
s = {34,56,66,55,77,77}
s
{34, 66, 55, 56, 77}
s[3]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s[3]
TypeError: 'set' object is not subscriptable
#dictionary
data = { 1:"one", 2:"two", 3:"three"}
data
{1: 'one', 2: 'two', 3: 'three'}
data[3]
'three'
data.get(2)
'two'
print(data.get(2))
two
print(data.get(4))
None
data.get(1, 'not found')
'one'
data.get(5, 'not found')
'not found'
keys = ['carlos', 'ana' , 'manuel']
values = ['python', 'java', 'js']
data = dict(zip(keys,values))
data
{'carlos': 'python', 'ana': 'java', 'manuel': 'js'}
data['carlos']
'python'
data['monica']
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    data['monica']
KeyError: 'monica'
data['monica'] = "C"
data
{'carlos': 'python', 'ana': 'java', 'manuel': 'js', 'monica': 'C'}
del data['ana']
data
{'carlos': 'python', 'manuel': 'js', 'monica': 'C'}
prog = {'js': 'atom', 'C':'vs', 'python':['sublime', 'pycharm'], 'java':{ 'jse': 'neatbeans', 'jee':'eclipse'}}
prog
{'js': 'atom', 'C': 'vs', 'python': ['sublime', 'pycharm'], 'java': {'jse': 'neatbeans', 'jee': 'eclipse'}}
prog['js']
'atom'
prog['python']
['sublime', 'pycharm']
prog['python'][1]
'pycharm'
prog['java']['jee']
'eclipse'
