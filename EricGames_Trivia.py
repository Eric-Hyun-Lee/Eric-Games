import time
import random
questionAnswered = set()
def clear():
	print("\033[2J\033[1;1H", end="")
def glitch():
  for i in range(50):
    print("GlItcH")
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
    time.sleep(0.01)

money = 0
questionAndAnswer = {"What arboreal marsupial is known for sleeping the vast majority of the day?":"Koala","What do the following words have in common: isosceles, equilateral, and scalene?":"They are all types of triangles","What war was ended by the signing of the Treaty of Versailles?": "World War 1", "What is in this picture? ax² + bx + c = 0; x = (-b ± √(b²-4ac)) / 2a":"The Quadratic Formula", "What do you call a baby owl?":"Owlet", "What is the capital of Iceland?":"Reykjavik","What is the Pythagorean Theorem?":"a2 + b2 = c2"}
question_list = list(questionAndAnswer.keys())
question_number = random.randint (0 ,len(question_list) -1)
question1 = input("Welcome to EricGames.com!Today we're playing...E_r_I_c T_r_I_v_I_a!!!Do you need more explanation???Type yes or no.")
question = question_list[question_number]
if question1 == "yes":
  print("answer the questions I give you and you earn money.")
  print("We are going to start now")
  time.sleep(1)
  print(3)
  time.sleep(1)
  print(2)
  time.sleep(1)
  print(1)
  time.sleep(1)
while True:
  question_number = random.randint (0 , len(question_list) -1)
  question = question_list[question_number]
  while question in questionAnswered:  
    question_number = random.randint (0 , len(question_list) -1)
    question = question_list[question_number]
  User_answer = input(question + " ")
  questionAnswered.add(question)
  correctAnswer = questionAndAnswer[question]
  if User_answer == correctAnswer:
    print("You earned $10!")
    money+=10
    if len(questionAnswered) == len(question_list):
      print("YOu")
      time.sleep(1)
      clear()
      print("have")
      time.sleep(1)
      clear()
      print("obtained")
      time.sleep(1)
      clear()
      glitch()
      print("$" + str(money))
      break
  else:
    print("Uh oh")
    glitch()
     
    print("Rab lld!You eaRm $O!!!!1!")  
    print("Meaning:Bad Kid!You earn $0!!!!!!")
    break
  
  
  
  
  