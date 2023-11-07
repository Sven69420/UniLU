#mainly used for tp2
from math import sqrt
#mainly used for tp6
import string

'''
#tp1 "Hello World"
print("Hello World") #should print "Hello World" into console
'''
'''
#tp2 "Triangle lengths and Temperature conversions"
#Triangle lengths
a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

#check if lengths zero
if a <= 0 or b <= 0 or c <= 0:
    print("The triangle lenghts need to be bigger than 0")
else:
    #check if triangle can be formed
    if a + b < c or a + c < b or b + c < a:
        print("The sum of 2 lengths cannot be smaller than a single lenght")
    else:
        #calculate semi-perimeter
        s = (a + b + c) / 2
        #calculate area using semi-perimeter
        area = sqrt(s*(s - a)*(s - b)*(s - c))
        #print area
        print(f"The area of your triangle is: {area}")
'''
'''
#Temperature conversions (For loop)
minT = input("Input minimum temperature: ")
maxT = input("Input maximum temperature: ")
step = input("Input step: ")

#if minT not given
if not minT:
    minT = 0
else:
    minT = int(minT)

#if step not given
if not step:
    step = 1
else:
    step = int(step)

#if maxT not given
if not maxT:
    print("Maximum temperature needs to be provided for the loop to finish")
else:
    maxT = int(maxT)

    #print table headers
    print("Celsius\tFahrenheit")

    #temperature loop
    for temp in range(minT, maxT + 1, step):
        #temperature conversion
        fahrTemp = temp * 9/5 + 32
        print(f'{temp}\t{fahrTemp}')
'''
'''
#Temperature conversions (While loop)
minTw = input("Input minimum temperature: ")
maxTw = input("Input maximum temperature: ")
stepw= input("Input step: ")

#if minT not given
if not minTw:
    minTw = 0
else:
    minTw = float(minTw)

#if step not given
if not stepw:
    stepw = 1
else:
    stepw = float(stepw)

#if maxT not given
if not maxTw:
    print("Maximum temperature needs to be given for loop to end")
else:
    maxTw = float(maxTw)

    #initialize while loop
    tempw = minTw
    tempFahrw = tempw * 9/5 + 32

    #print table headers
    print("Celsius\tFahrenheit")

    #while loop for table
    while tempw < maxTw:
        print(f"{tempw}\t{tempFahrw}")
        tempw += stepw
'''
'''
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
"""
print(isPrime(-1)) # should return False
print(isPrime(1)) #should return False
print(isPrime(2)) #should return True
print(isPrime(6)) #should return Fasle
"""

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
"""
print(countPrimeNumbers([1, 2, 3, 6, 7])) #should return 3
print(countPrimeNumbers([-5, 0, 13, 4])) #should return 1
print(countPrimeNumbers([])) #should return 0
"""

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
'''
'''
#tp4 "Recursion"
def sum_series(n):
    """Function to calculate recursive sum"""
    if n == 1:
        return 1
    return sum_series(n - 1) + n
#print(sum_series(1)) #should return 1
#print(sum_series(5)) #should retrun 15


def is_magic_sequence(s):
    """Function to check if given sequence is a magic sequence"""
    if len(s) == 0:
        return True
    return abs(s[0]) == abs(s[-1]) and is_magic_sequence(s[-1:1])
"""
print(is_magic_sequence([-1, -2, 0, 2, 1])) #should return True
print(is_magic_sequence([1, -2, 0, 2, 3])) #should return False
print(is_magic_sequence([-1, 1])) #should return True
print(is_magic_sequence([1])) #should return True
print(is_magic_sequence([])) #should return True
"""
'''
'''
#tp5 "Structure data types and functions as objects"
def convert_grades_in_place(s):
    """Funciton that converst number grade into percentage grade"""
    for i in range(len(s)):
        name, grade = s[i]
        percentage = grade / 20 * 100
        s[i] = (name, percentage)
    return s
#should return [('student1', 50.0), ('student2', 45.0), ('student3', 90.0)]
#print(convert_grades_in_place([('student1', 10.0), ('student2', 9.0), ('student3', 18.0)]))

def convert_grades_new(s):
    """Does the same thing as before but without modifiying the parameter s"""
    return [(name, grade / 20 * 100) for name, grade in s]
#should return [('student1', 50.0), ('student2', 45.0), ('student3', 90.0)]
#print(convert_grades_new([('student1', 10.0), ('student2', 9.0), ('student3', 18.0)]))

def grade(grades):
    """Function that retruns true if average of grades is equal to or bigger than 10"""
    #check if student has any grades
    if not grades:
        return False
    
    #calculate average
    average = sum(grades) / len(grades)

    #return true if average bigger than or equal to 10
    return average >= 10
#print(grade([5.0, 15.0])) #should return True
#print(grade([])) #should return False

def filter_students_by_grade(d, grading_function):
    """Function that deletes students with insufficient grades from the list"""
    #check for each student in list
    for student in list(d):
        #assigne grade for each student
        grades = d[student]

        #apply grading_function 
        sufficient_grade = grading_function(grades)

        #if grade not sufficient delete student from list
        if not sufficient_grade:
            del d[student]
    return d
#should return {'student2': [12.0, 17.5]}
print(filter_students_by_grade({'student1': [5.0, 10.0], 'student2': [12.0, 17.5]}, grade))
#should return {'student2': [20.0]}
print(filter_students_by_grade({'student1': [], 'student2': [20.0]}, grade))
'''
'''
#tp6 "Words and Files"
def isWord(s):
    """Function that checks if string consists of existing words"""
    for part in s.split("-"):
        if not part.isalpha():
            return False
    return True
"""
print(isWord("health")) #should return True
print(isWord("out-of-date")) #should return True
print(isWord("part--time")) #should return False
print(isWord("")) #should return False
"""

def countWords(f):
    """Function that counts Words from text file"""
    #open text file in read mode
    file = open(f, "r")

    #empty dicitonary for words occurences
    frequencies = {}

    #loops to iterate through lines in file
    for line in file:
        #loop to iterate through words in splitted lines
        for word in line.split():
            #clean word of punctuation and make it case-insensitive
            w_cleaned = word.strip(string.punctuation).lower()

            #check if cleaned word is an exisiting word
            if isWord(w_cleaned):
                #check if cleaned word already in frequencies dictionary
                if w_cleaned in frequencies:
                    #if cleaned word already in dictionary add 1
                    frequencies[w_cleaned] += 1
                else:
                    #if cleaned word not already in dictionary create an instance of word in dictionary with 1 as its word count
                    frequencies[w_cleaned] = 1
    file.close() #close file after loop
    return frequencies

#ignore this (this is for my specific file path of the textfile on my personal computer)
#use a raw string for the file path to avoid issues with backslashes
file_path = r"C:\Users\svenb\OneDrive\Desktop\Various\Important\School\Uni 1st Year\Courses\Programming Fundamentals\Additional Coding Stuff\additional\tp6-textfile.txt"
print(countWords(file_path))
'''
