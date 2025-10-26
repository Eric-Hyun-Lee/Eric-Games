# Print begginin' and press enter to play print readyy set type
import random
print("If you get the word BOB which has a 0.5% chance of happening, comment it.")
def clear():
	print("\033[2J\033[1;1H", end="")
import time
beginin =input("welcome to ENGLISH LONG WORD Typer. Press enter/return to play")
print("ready...")
time.sleep(1)
print("set...")
time.sleep(1)
print("GO!")
# List to store ∞ sentences
print("This is the word you have to type(Not this one.The one under this)")
sentences = ["aequeosalinocalcalinoceraceoaluminosocupreovitriolic","pneumonoultramicroscopicsilicovolcanoconiosis",
"hippopotomonstrosesquippedaliophobia","Supercalifragilisticexpialidocious","dichlorodiphenyltrichloroethane","pseudopseudohypoparathyroidism","floccinaucinihilipilification","spectrophotofluorometrically,Antidisestablishmentarianism","psychoneuroendocrinological","BOB"]
sentence = (sentences[random.randint(0,len(sentences)-1)])
print(sentence)
start = time.time()
UserType = input("Type:  ")

while UserType != sentence:
  print("incorrect")
  UserType = input("Type:  ")
end = time.time()
Usertime = end-start

print("You")
time.sleep(1)
print("completed")
time.sleep(1)
print("One of Englishes")
time.sleep(1)
print("Longest")
time.sleep(1)
print("word")
time.sleep(1)
print("in")
time.sleep(1)
for i in range(50):
  print('GlItcH')
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
print(str(Usertime) + " seconds")
# count time after we give user sentence
# check if sentence is same start = time.time() end = time.time() end - start
#Give time if sentence is correct, if not say INCORRECt and give another trial
