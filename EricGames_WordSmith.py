import random
import time
def clear(): 
  print("\033[2J\033[1;1H", end="")
# reads words into list
f = open("valid_words.txt")
validWords = f.readlines()
validWords = {x.strip() for x in validWords}
points = 0
usedWords = set()

f.close()
#Type intro
input("Welcome to EricGames.com!This game is ERIC_W_o_R_d_S_m_I_t_H_✏️.In this game, come up with as many words as you can using the 7 letters that are given in 1 minute.Based on how long the word is, you will get more points.Are you ready?Press enter/return to begin!")
print("Ready")
time.sleep(1)
print("Set")
time.sleep(1)
print("GO!!!!!")
letters = set()
while len(letters) < 2:
  letters.add(random.choice("aeiou"))
while len(letters) < 7:
  rand_letter = chr(random.randint(ord("a"), ord("z")))
  letters.add(rand_letter)
print(letters)
start = time.time()
while time.time() - start < 60:
  isValid = False
  w = input("Enter a word ")
  for i in range(len(w)):
    if w[i] not in letters:
      isValid = True
      print("Invalid word.Please use the letters given.Nice try!")
      break
  if isValid:
    continue
  if w in usedWords:
    print("already used")
  if w in validWords:
    print("Valid word")
    points += int(len(w)) 
    usedWords.add(w)
  #If correct, add point
  #If incorrect, say invalid word
  if w not in validWords:
    print("invalid word")
  #If repeated, say repeated
  #Tell what their score using glitch
  if time.time() - start > 60:
    break
clear()
print("TIME IS UP")
time.sleep(1)
print("You have obtained")
time.sleep(1)
for i in range(10):
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
clear()
print(str(points) + " points")