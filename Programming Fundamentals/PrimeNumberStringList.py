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

def countPrimeNumbers(intList):
    """Function returns number of Primes found in a give number List"""
    count = 0
    for x in intList:
        if isPrime(x):
            count += 1
    return count

def countPrimesFromKeyboard():
    """Function returns number of Primes in input List"""
    kL = input("Input your number List")
    intList = []
    
    count = countPrimeNumbers(kL.split(","))
    for x in kL:
        intList.append(int(x))
    
    print(f'There are, {count}, prime numbers in the list')

