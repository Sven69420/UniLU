import random

x = int(input("Give me a Number that I'll use as the maximum for my range of randomly generated numbers : "))
#Maximum range designated by User input
guess = int(input("Guess a random number : "))
#Guess made by User

randomNbr = random.randint(1, x)
print(f'The randomly generated number is : {randomNbr}')
#randomly generated number

probability = 1 / x
percentageChance = probability * 100
rounded_percentageChance = round(percentageChance, 2)
negativeChance = 100.00 - rounded_percentageChance
#this calculates the percentage chance of both numbers being the same

if guess == randomNbr and x <= 10000:
    print(f'Wow the random numbers matched! The likelihood of this happening is {rounded_percentageChance}%')
elif guess == randomNbr and x > 10000:
    print(f'Wow the random numbers matched! The likelihood of this happening is almost {rounded_percentageChance}%')
elif guess != randomNbr and x > 10000:
    print(f'You guessed wrong! No worries the likelihood of this happening is almost {negativeChance}%')         
else:
    print(f'You guessed wrong! No worries the likelihood of this happening is {negativeChance}%') 
