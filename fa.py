import random #We will need random number for the player to guess.
randomNumber = random.randint(0,100) #random number
numGuess = 0
extraCookie = random.randint(1, 10)
guess = input("Guess the number I am thinking right now! ")
while guess != randomNumber: #Repeat until they get the number correct
    if guess > str(randomNumber): #Check if the number is too high.
        guess = input("Sorry! " + str(guess) + " was too high!")
        numGuess+=1
    if guess < str(randomNumber): #Check if it was too low.
        guess = input("Sorry! " + str(guess) + " was too low!")
        numGuess+=1
    if guess == str(randomNumber): #Check if they got it correct
        numGuess+=1
        print("Wow! You got the number correct! You get a cookie!")
        print("It took you "+ str(numGuess) + " guesses to get the number correct!Good job!")
        ask = input("Do you want another cookie? I might have another one.Reply yes or no without capitalization. There are def. no secrets.")
        if ask == "yes":
            if extraCookie == 1:
                print("You also get a extra bonus cookie!")
            else:
                print("Sorry, I don't have another cookie. Play again next time and I might have one.")
        if ask == "no":
            print("OK, here's a lollipop instead for being a good sport, thanks for the fun! I had fun playing with you! Play again next time!")
        if ask == "67":
            print("You earned the definetly only achievment:676767676767676767676767kid.5 more cookies to you!")
        if ask == "duolingo" or ask == "Duo" or ask == "Doulingo" or ask == "duo":
            print("Go extend your streak! You earned the actually 2nd achievment: DuolingoIsHappy.")
    if guess == randomNumber == 67: #Check if they got 67 correct!
        print("Wow! You got the number correct AND it was 67! You get a cookieCookie and a pet Snailaguette, WARNING: Don't eat the baguette on its back!")          
        print("Oh yeah, there are two achievments.676767676767676767676767kid and DoulingoIsHappy. ")