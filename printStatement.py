print("Hello, world!")
greeting = 'Hola Mundo'
english = 'Hello world'
portuguese = 'olá Mundo'

print(greeting)

for i in range(2):
    print("*"*14)
print( )
language = input("""Choose language: 
1-English
2 -Spanish
3 -Portuguese
""")

if language == '1':
    print(english)
    for i in range(2):
        print("*"*14)
elif language == '2':
    print(greeting)
    for i in range(2):
        print("*"*14)
elif language == '3':
    print(portuguese)
    for i in range(2):
        print("*"*14)



