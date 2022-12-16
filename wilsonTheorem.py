
def is_prime( ):
    n = int(input("Please enter a number: "))
    new = n-1
    fact = 1
    for w in range(1,new+1):
        fact *=w
    wilson = fact +1
    if wilson % n == 0:
        return True
    

def run( ):
    if is_prime( ):
        message = " Is a prime "
        print(message)
    else:
        print("Is not a prime")


if __name__ == '__main__':
    run( )

#references https://www.cuemath.com/prime-numbers-formula/
#https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic
#https://en.wikipedia.org/wiki/Wilson%27s_theorem#Primality_tests
#https://es.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/congruence-modulo
#https://www.geeksforgeeks.org/factorial-in-python/