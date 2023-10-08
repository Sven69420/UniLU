def isPrime(n):
    """Function that checks to see if n is a Prime number or not"""
    if n <= 1:
        return print(False)
    elif n <=3:
        return print(True)
    elif n % 2 == 0 or n % 3 == 0:
        return print(False)

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return print(False)
        i += 6
        
    return print(True)


 
