userInputMinT = input("Start at : ")

if userInputMinT.strip():  # Check if the input is not empty after stripping whitespace
    try:
        minT = int(userInputMinT)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        minT = None
else:
    minT = 0

if minT is not None:
    print(f"The minimum you entered (or default): {minT}")

maxT = int(input("End at : "))
step = int(input("step : "))

c = minT
while c < maxT:
    print(c, '°C\t', c * 9 / 5 + 32, '°F')
    c += step
