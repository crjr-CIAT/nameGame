import time, os # importing modules to help console clear and organized.

def nameGame(): # defining the game.
    name = input("Whats your name? >>> ") # getting the users input.
    vowels = ["a", "e", "i", "o", "u", "y"] # storing chars that are vowels in an array.
    vowelCount = 0 # the amount of found vowels in {name}.

    for letter in name: # for each letter in the name.
        if letter in vowels: # if the the letter is in vowels.
            vowelCount += 1 # increase the count of found vowels.

    def oddOrEven(): # defining the even or odd checker.
        if len(name) % 2 == 0: # if the the remainder of division is 0.
            return True # return True.
        else: # if the the remainder of division is other than 0.
            return False # return False.
    res = oddOrEven() # calling the function.

    print("'" + name + "' is " + str(len(name)) + " characters long.") # print the len of the provided name.
    if res: # if True.
        print("Your name is even")
    else: # if False.
        print("Your name is odd")
    print("There are " + str(vowelCount) + " vowels in your name.") # print the amount of vowels in the provided name.

    again = input("Go again? (Y/N) >>> ") # asking the user if they would like to go again.
    options = ["Y", "y", "yes", "Yes", "N", "n", "no", "No"] # options Y/N-Yes/No.
    Yoptions = ["Y", "y", "yes", "Yes"] # yes alts.
    Noptions = ["N", "n", "no", "No"] # no alts.
    while again not in options: # while anything other than Y/N** was given.
        again = input("Would you like to go again? (Y/N) >>> ") # asking for confirmation again *x till Y/N**.

        if again in Yoptions: # if yes.
            time.sleep(0.5) # wait .5s or 500ms.
            os.system('cls') # clear the console.
            nameGame() # starting the game over
        else:
            if again in Noptions: # if no.
                while True: # a loop thats always true.
                    if True: # a statement thats always true.
                        break # leaves the loop thus ending the game.

    if again in Yoptions:  # if yes. (outside the loop)
        time.sleep(0.5) # wait .5s or 500ms.
        os.system('cls') # clear the console.
        nameGame() # starting the game over
    else:
        if again in Noptions: # if no.
            while True: # a loop thats always true.
                if True: # a statement thats always true.
                    break # leaves the loop thus ending the game.
nameGame() # starts the game when "pyhton additional.py" is called in the console.