import string

def wordCount(words):
    #spliting each word into its own line based on white spaces
    wordList = words.split()

    #establing number for the count and returning it
    count = len(wordList)
    return count

def letterCount(words):
    #formatting string for ease of use
    words = words.lower()


    #create dictionary to store information
    charCount = {}

    #for loop to check each character
    for char in words:
        if char.isalpha() == True:    
            if char in charCount:
                #create key and set to 1
                temp = charCount[char]
                charCount[char] = temp + 1
            else:
                #add one to value
                charCount[char] = 1


    return charCount        



def main():
    #intialzing file 
    filePath = "books/frankenstein.txt"
    with open(filePath) as f:
        #copying the book to a string for later work
        book_contents = f.read()

        #word count call
        count = wordCount(book_contents)

        #char count call
        charCount = letterCount(book_contents)

        #display information
        print("------------------------------------------------")
        print(" --- Begin report of", filePath, "---")
        print("------------------------------------------------")

        print("")
        print("The total amount of words found is ", count)
        print("")
        print("Below is a list of the count of characters from the largest to smallest")
        print("")
        #sort in ascending order
        charCount = dict(sorted(charCount.items(), key=lambda item: -item[1]))

        #for loop to display dictionary items
        for char in charCount:
            temp = charCount[char]
            print("The'", char,"'character was found", temp,"times")

        print("")
        print("-----------------------------------------------")


main()