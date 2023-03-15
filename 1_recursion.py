def fibo(n):
    # if n == 1:
    #     print(1)
    # else:
    #     next = n-1 + n-2
    #     fibo(n)
    #     print(next)

    if n >= 3:
        fibonacci = fibo(n-1) + fibo(n-2)
        print(fibonacci)
    else:
        fibonacci=1
        print(fibonacci)
    
fibo(3)