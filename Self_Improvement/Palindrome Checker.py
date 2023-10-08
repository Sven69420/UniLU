#A palindrome is a word that reads the same forwards and backwards

userPali = input("Please input a word to check if its a Palindrome : ")
#Asks the user for an input

if userPali.strip() == "":
    print('An example for a Palindrome is : "Racecar"')
    #checks to see if Input is empty 
else:
    cleaned_userPali = ' '.join(userPali.split()).lower()
    #cleans the user input by removing spaces and makes it case-insensitiv

    if cleaned_userPali == cleaned_userPali[::-1]:
        print(f"'{userPali}' is a Palindrome")
    else:
        print(f"'{userPali}' is NOT a Palindrome")
    #End result for both cases
    
