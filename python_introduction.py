Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
2+3
5
9-8
1
4*6
24
8/4
2.0
5/2
2.5
5//2
2
8+9-10
7
(8+2)*3
30
8+(2*3)
14
2**3
8

10 / 3
3.3333333333333335
10//3
3
10%3
1
'hey'
'hey'
'hey'
'hey'
print('Hola')
Hola
print("Darwin's laptop")
Darwin's laptop
print("Darwin's 'laptop'")
Darwin's 'laptop'
Darwin's 'laptop'
SyntaxError: unterminated string literal (detected at line 1)
print('navin\'s "laptop"')
navin's "laptop"
'darwin'+'darwin'
'darwindarwin'
20*"Darwin"
'DarwinDarwinDarwinDarwinDarwinDarwinDarwinDarwinDarwinDarwinDarwinDarwinDarwinDarwinDarwinDarwinDarwinDarwinDarwinDarwin'
print('C:\docs\darwin')
C:\docs\darwin
C:\docs\darwin
SyntaxError: unexpected character after line continuation character
print('c:\docs\darwin')
c:\docs\darwin
c:\docs\darwin
SyntaxError: unexpected character after line continuation character
print('c:\docs\navin')
c:\docs
avin
print(r'c:\docs\navin')
c:\docs\navin
x = 2
x + 3
5
y = 3
x + y
5
x  = 9
x + y
12
x
9
z
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    z
NameError: name 'z' is not defined
x + 10
19
_ + y
22
name = ' youtube'
name + ' rocks!'
' youtube rocks!'
name[0]
' '
name[1]
'y'
name[8]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    name[8]
IndexError: string index out of range
name[-1]
'e'
name[-7]
'y'
name[0:2]
' y'
name[0:3]
' yo'
name[1:]
'youtube'
name[ : 4]
' you'
name[3:10]
'utube'
name[0:3] = 'my'
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    name[0:3] = 'my'
TypeError: 'str' object does not support item assignment
'my' + name[3:]
'myutube'
my_name = 'Ruben Dario'
len(my_name)
11
nums = [34,56,7,8,67]
nums
[34, 56, 7, 8, 67]
#list in python
nums[54)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
nums[54]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    nums[54]
IndexError: list index out of range
nums[2 : ]
[7, 8, 67]
nums[-1]
67
names = ['carlos', 'Maria', 'Juan']
values = [9.7, 'James', 45]
mil = [nums, names]
mil
[[34, 56, 7, 8, 67], ['carlos', 'Maria', 'Juan']]
#list are mutable
nums.insert(2,77)
nums
[34, 56, 77, 7, 8, 67]
nums.remove(8)
nums
[34, 56, 77, 7, 67]
nums.pop(1)
56

nums.pop()
67
del nums[2:1]
nums
[34, 77, 7]
nums.extend([3,5,6,7])
nums
[34, 77, 7, 3, 5, 6, 7]
min(nums)
3
max(nums)
77
sum(nums)
139
nums.sort()
nums
[3, 5, 6, 7, 7, 34, 77]
#python lec5 Lists  