import random
import time
number = 21
def cardMaker():
  hand = [] 
  hand.append(random.randint(1,11))
  if hand[0] == 11: 
    hand.append(random.randint(1,10))
  else:
    hand.append(random.randint(1,11))
  return hand
def clear():
	print("\033[2J\033[1;1H", end="")
start = input("Welcome to EricGames.com! today we are playing...Eric_B_l_A_c_K_j_A_c_K!You will get 2 numbers to start.Your goal is to get as close but not over 21.When you are done, the dealer plays.If he reaches 21, he wins, if you do, you win!If you both don't, the person with the biggest sum wins!Are you ready???Press enter/return to play!")


while True:
  player_hand = cardMaker()
  while True:
    continueGame = False
    print(player_hand)                      
    print("Here is your hand")
    question1 = input("If you want to stop and let the dealer play, press s.If you want to get another card, press h: ")
    if question1 == "s":
      continueGame = True
      break
    if question1 == "h":
      player_hand.append(random.randint(1,11))
      print("HERE IS YOUR HAND",player_hand)
      sumOfNumber = sum(player_hand)
      if sumOfNumber > number:
        print("You busted")
        time.sleep(1)
        clear()
        print("You busted.")
        clear()
        time.sleep(1)
        print("You busted. .")
        clear()
        time.sleep(1)
        print("You busted. . .")
        clear()
        time.sleep(1)
        
        print("Better luck next time!")
        break
      elif sumOfNumber  == number:
        print("YOU WON LIKE A CHAMP!!!!!I give you permission to play video games all day!Tell your parents!Nothing can stop them! 🎊🎊🎊🎊")
        break
    else:
      print("u - oh")
      time.sleep(2)
      for i in range(20):
        time.sleep(0.01)
        clear()
        time.sleep(0.01)
        clear()
        print("GLiTcH")
        time.sleep(0.01)
        clear()
        print("61i7ch")
        time.sleep(0.01)
        clear()
        print("6L712H")
        time.sleep(0.01)
        clear()
        print("GL/.cH")
        time.sleep(0.01)
        clear()
        print("Gl1T2H")
        time.sleep(0.01)
        clear()
      for i in range(50):
        print('UNKnoWn ERroR')
        time.sleep(0.01)
        clear()
        print("UnKn0Wn E660R")
        time.sleep(0.01)
        clear()
        print("\/KN0wn Er606")
        time.sleep(0.01)
        clear()
        print("U^K/0%n E66or")
        time.sleep(0.01)
        clear()
        print("unKnWoN ErR0R")
        time.sleep(0.01)
        clear()
        print("\.nw0n. 3R6or")
        time.sleep(0.01)
        clear()
        print("AAAAHHHHHHHHHH")
        time.sleep(0.01)
        clear()
        print("SOS")
        time.sleep(0.01)
        clear()
      print("Please enter S or H😅")
  if continueGame:
      dealerHand = cardMaker()
      print(dealerHand)
      while sum(dealerHand) < 17:
        dealerHand.append(random.randint(1,11))
        print(dealerHand)
      if sum(dealerHand) == 21:
        print("You lost...")
        time.sleep(1)
        print("Better luck next time!")
      elif sum(dealerHand) > 21 or  sum(player_hand) > sum(dealerHand):
        print("YOU WON LIKE A CHAMP!!!!!")
      else:
        print("you lost")
  answer2 = input("Do you want to keep playing?If yes, press y.If no, press l")
  if answer2 == "l":
    break