import random

def printWelcome():
  print("THIS IS EricGames.com introducing...NUMBER GUESS CHALLENGE!!!")
  print("I am thinking of a random number between 1 and 100. Guess what it is!")



def getRandomNumber():
  myRandomNumber = random.randint(0,100)
  return myRandomNumber



def getGuessFromUser():
  guess = int(input("Enter a new guess: "))
  return guess



def answerIsRight(answer, guess):
  if answer == guess:
    return True
  elif guess < answer:
    print("You guessed too low!")
    return False
  else:
    print("You guessed too high!")
    return False


def printScore(numGuesses):
  print('It took you ' + str(numGuesses) + ' guesses to guess my number.')
  if numGuesses == 1:
    print("Lucky you, you guessed my secret number on the first try!Wow!It'll take me FOREVER to guess my number.")
  elif numGuesses < 5:
    print("Pretty solid guessing, it took you less than 5 tries to guess my number!Good job")
  elif numGuesses < 15:
    print("Pretty average guessing!Good job!")
  else:
    print(" It took you more than 15 guesses to guess my number.It's Ok.You can always try again.👍")


def playGame():
  printWelcome()
  answer = getRandomNumber()
  
  

  guess = getGuessFromUser()
  numGuesses = 1 
  while not answerIsRight(answer, guess):
    guess = getGuessFromUser()
    numGuesses = numGuesses + 1
  printScore(numGuesses)
playGame()



