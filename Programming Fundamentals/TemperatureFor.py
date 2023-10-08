userInputMinT = input("Start from : (or default = 0)")

if userInputMinT.strip():  # Check if the input is not empty after stripping whitespace
    try:
        minTFah = int(user_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        minTFah = None
else:
    minTFah = 0

if minTFah is not None:
    print(f"The minimum you entered (or default): {minTFah}")
    
#This is your minimal Temperature input in Fahrenheit
    
maxTFah = int(input("End at :"))

if maxTFah is not None:
    print(f"The maximum you entered (or default): {maxTFah}")
#This is your maximal Temperature Fahrenheit

convStep = int(input("Step :"))
#This is your Step value form min to max

for c in range(minTFah, maxTFah, convStep):
    print(c, '°C', ' ', c * 9 / 5 + 32, '°F')

