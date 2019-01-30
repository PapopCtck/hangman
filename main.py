import random
import math
from artists import artists
from country import country
categories = ["Country","Artists"]




def NewGame():
    print("Game start!")
    print("Select Category")
    print("================================")
    for i in categories:
        print(categories.index(i)+1,"",end = "")
        print(i ,end =" ")
    print("")
    print("================================")
    
    while True:
        Category = input("Category :").casefold()
        if Category == "":
            print("Please input something!")
        elif Category.isnumeric and len(Category) < len(categories):
            Category = categories[int(Category)-1].casefold()
            print("You choose : "+ Category.capitalize())
            wordList = globals()[Category]
            Game(wordList)
            return
        else:
            for i in categories:
                if Category == i.casefold():
                    print("You choose : "+ Category.capitalize())
                    wordList = globals()[Category]
                    Game(wordList)
                    return
                else:
                    continue
        print("Please select from Category avaliable!")

def Game(x):
    score = 0
    guessedChar = []
    secret = ""
    guessWord = []
    # print(x.keys())
    secret = random.choice(list(x))
    # print(secret)
    hint = x.get(secret)
    for char in secret:
        if char.isnumeric():
            guessWord.append(char)
        else:
            guessWord.append("-")
    length = len(secret)
    print("The word is", length, "characters long")
    maxGuess = 10
    guessCount = 0
    count = 1
    while guessCount < maxGuess:
        chance = maxGuess - guessCount
        for i in guessWord:
            print(i,end = '')
        print("")
        print("Chance : ",chance , end='')
        print(" Score : ",score)
        print("Guessed letter : ",end="")
        for i in guessedChar:
            print(i,end = "")
        print("")
        print("Hint : " + hint)
        guessChar = input("Your guess :").casefold()
        if len(guessChar) >= 2:
            print("")
            print("Input only one character!")
            print("")
        else:
            if not guessChar.isalpha():
                print("")
                print("Enter a letter from a-z!")
                print("")
            elif guessChar in guessedChar:
                print("")
                print("Dejavu! I've seen that letter before!")
                print("")
            else: 
                guessedChar.append(guessChar)
                if guessChar in secret:
                    print("")
                    print("Correct!")
                    print("")
                    score += 10*chance/count
                    score = math.ceil(score)
                    count = 1
                    for i in range(length):
                        if secret[i] ==  guessChar:
                            guessWord[i] = guessChar
                else:
                    print("")
                    print("Try again!")
                    print("")
                    count += 0.5
                    guessCount +=1
        if not '-' in guessWord:
                    print("You won! Score : ",score)
                    break
    if guessCount == maxGuess:
        print("You lose , Secret word was : " + secret)
    restart = input("Restart? (Y or N) : ").casefold()
    if restart == "Y" or restart == "y":
        NewGame()
    else:
        print("Good bye!")
        return



NewGame()







