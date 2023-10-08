import random

popCulRef = {
    "1337": "leet speak",
    "420": "Weed",
    "69": "Sex position",
    "Ligma": "Lick ma balls",
    "Who had Ligma first?": "Ninja",
    "joe mama": "your mama"
}
#List of pop Culture References

word_list = list(popCulRef.keys())
#List of Words

while True:
    random_index = random.randint(0, len(word_list) -1)
    #generate a random index within the range of the List

    random_word = word_list[random_index]
    #get a random word

    correct_meaning = popCulRef[random_word]
    #get the correct meaning of the word

    uI = input(f"Tell me what '{random_word}' references : ")
    #get the user input

    if uI.strip().lower() == 'exit':
        break
    #check if the user wants to exit

    if uI.lower() == correct_meaning.lower():
        print("Correct, you know pop culture very well")
        print("Note : to exit type 'exit'")
    else:
        print("False, you need to look at more memes")




