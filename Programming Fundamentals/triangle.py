a = float(input("give me the first length of the triangle"))
#this is the first input value
b = float(input("give me the second length of the triangle"))
#this is the second input value
c = float(input("give me the third length of the triangle"))
#this is the third input value

if a < 0 or b < 0 or c < 0:
    print("error the triangle can't have negative lengths")
    #Check for negative lengths
else:
    if a + b <= c or a + c <= b or b + c <= a:
        print("error : the sum of 2 lenghts can't be smaller than a single lenght")
        #Check for triangle inequality theorem
    else:
        s = (a + b + c) / 2
        #Calculate the semi-perimeter 

from math import sqrt
#Calculate the area using Heron's formula

Area = sqrt(s*(s - a)*(s - b)*(s - c))
print(f'The area of your triangle is: {Area:.2f}')
#print the end result
