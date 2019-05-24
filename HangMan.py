import random
HANGMAN=("""

------
|    |
|
|
|
|
|
|
|   
---------
""",
"""

------
|    |
|    0
|
|
|
|
|
|
---------
""",
"""
------
|    |
|    0
|    |
|
|
|
|
|
----------
""",
"""
------
|    |
|    0
|   /|
|
|
|
|
|
-----------
""",
"""
------
|    |
|    0
|   /|\
|
|
|
|
|
-----------
""",
"""
------
|    |
|    0
|   /|\
|   / 
|
|
|
|
-----------
""",
"""
------
|    |
|    0
|   /|\
|   / \
|
|
|
|
------------
""")
play_again=True
while play_again:
    words_list=['ninjas','python','university','programming','jazz','games','kinder']
    chosenword=random.choice(words_list).lower()
    guess=None #player guess input
    guessed_letters=[] #we add all of the users guesses to this list
    blank_word=[] #replacing all of the letters of the chosen word with dashes
    for letter in chosenword:
        blank_word.append("_")
    attempts=6


    while attempts>0:
        if(attempts!=0 and "_" in blank_word):
            print(("\nyou have {} attempts remaining.").format(attempts))
        

        try:
            guess=str(input("\nPlease select a letter between A-Z")).lower()
        except:
            
            print("That is not valid input.Please try again.")
            continue
        
        else:
            if not guess.isalpha():
                print("That is not a letter.Please try again.")
                continue
            
            elif len(guess)>1:
                print("That is more than one letter.Please try again.")
                continue
            elif guess in guessed_letters:
                print("You have already guessed that letter.Please try again.")
                continue
            else:
                pass

            
            guessed_letters.append(guess)
            if guess not in chosenword:
                attempts-=1
                print(HANGMAN[(len(HANGMAN)-1)-attempts])

            else:
                searchMore=True
                startsearchIndex=0
                while searchMore:
                    try:
                        foundAtIndex=chosenword.index(guess,startsearchIndex)
                        blank_word[foundAtIndex]=guess
                        startsearchIndex=foundAtIndex+1
                    except:
                        searchMore=False

            print("".join(blank_word))

            
            if attempts==0:
                print("Sorry, the game is over. The word was "+ chosenword)
                print("\nWorld you like to pay again?")
                response=input("> ").lower()
                if response not in ("yes","y"):
                    play_again=False
                    print("Thanks for playing Hangman!")
                break
            if "_" not in blank_word:
                print(("\nCongratulations! {} was the word").format(chosenword))
                print("\nWorld you like to pay again?")
                response=input("> ").lower()
                if response not in ("yes","y"):
                    play_again=False
                    print("Thanks for playing Hangman!")
                break
        

    
            
    
