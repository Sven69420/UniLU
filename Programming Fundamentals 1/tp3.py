#tp3 "prime numbers" 
def isPrime(n):
    """Function that checks if a given number is a prime number"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    #apply the 6k +/- 1 rule to check if given number is prime
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

print(isPrime(-1)) # should return False
print(isPrime(1)) #should return False
print(isPrime(2)) #should return True
print(isPrime(6)) #should return Fasle


def countPrimeNumbers(intList):
    """Function that counts prime numbers in integer list"""
    #initialize count 
    count = 0
    #for each entry(num) in intList
    for num in intList:
        #check if entry(num) is prime with previous function
        if isPrime(num):
            #increase count if isPrime() true
            count += 1
    return count

print(countPrimeNumbers([1, 2, 3, 6, 7])) #should return 3
print(countPrimeNumbers([-5, 0, 13, 4])) #should return 1
print(countPrimeNumbers([])) #should return 0


def countPrimesFromKeyboard():
    """Function that asks for string number list and converts it into integers"""
    #get user input list as string
    user_list = input("Please enter comma-separated number list: ")
    #initialize converted list
    conv_user_list = []

    #for each entry in string list splitted by ","
    for strNum in user_list.split(","):
        #add number converted from string into integer to converted list 
        conv_user_list.append(int(strNum))
    
    #apply previous countPrimeNumbers function
    strNum_count = countPrimeNumbers(conv_user_list)
    print(f"There are {strNum_count} prime numbers")