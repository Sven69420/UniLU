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