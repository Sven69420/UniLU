numlist = input("Input your number list seperated by commas : ")
numlist = numlist.split(",")

ntcount = 0
fcount = 0

for num in numlist: 
    num = int(num)
    if num == 19:
        ntcount += 1
    elif num == 5:
        fcount += 1

if ntcount == 2 and fcount >= 3:
    print(f"There's exactly {ntcount} Nineteens in the list and {fcount} 5's in the list")
else:
    print("The requriements have not been met")