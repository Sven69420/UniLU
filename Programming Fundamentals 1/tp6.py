#tp6 "Words and Files"
def isWord(s):
    """Function that checks if string consists of existing words"""
    for part in s.split("-"):
        if not part.isalpha():
            return False
    return True

print(isWord("health")) #should return True
print(isWord("out-of-date")) #should return True
print(isWord("part--time")) #should return False
print(isWord("")) #should return False


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