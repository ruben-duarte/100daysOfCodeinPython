print('Hallo')
print("\U0001F603")
name = input("What is your name? ")
print("Hallo", name)  #Concatenation

def greet(name):
    
    if name == "Mary":
        return "Hello, my love!"
    else: 
        return "Hello, {name}!".format(name=name)
