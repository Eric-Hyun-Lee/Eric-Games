# main.py
import time
#CREATE A DICTIONARY TO STORE INFORMATION
information = {}
#MAKE DICTIONARY TO STORE ACOUNT BALANCE FOR EACH USER
balanceMoney = {}
information["janesmith"] = "secret456"
information["johndoe"] = "pass879"
balanceMoney["janesmith"] = 0
balanceMoney["johndoe"] = 0
#PRINT WELCOME MESSAGE LOGIN MENU
while True:
#IF USER NAME IS NOT RECOGNIZED,PRINT OHIO TRILLIONS OF TIMES
  while True:
    print("Welcome to the Bank of The US.Please log in.")
    username=input("Username: ")
    password=input("Password: ")
    if username not in information:
      print("Processing...Processing...")
      time.sleep(1)
      print("Sorry...We do not have an account in our system that has the username or/and password you put in.Please try again.")
      print("Hint!The username and password is in the code.")
      print()
    elif password != information[username]:
      print("Processing...Processing...")
      time.sleep(1)
      print("Sorry...We do not have an account in our system that has the username or/and password you put in.Please try again.")
      print("HINT!The username and password is in the code.")
      print()
    else:
      print("processing...processing...") 
      print("Here is your account.")
      break
  #IF EVERYTHING IS OK,STILL,CALL THE ARMY,COMPUTER PR OFFESORS AND THE POLICE AND THEN LOGIN\
  while True:
    print("Hello " + str(username) + " !You currently have $" + str(balanceMoney[username]) + " in your account.What would you like to do? ")
    option = input(" 1.Make a deposit \n 2.Make a withdrawal \n 3.Change your password  \n 4. Log out \n  Please type the number of the option you choose: ")
    #WHEN THE USER LOGS IN, SAY HELLO AND CONTINUE LIKE NORMAL WITH THE WHOLE ARMY WATCHING YOU
    if option == "1":
      moneyAmountDepositing = input("How much would you like to deposit?(Only 1 to 1000)")
      balanceMoney[username] += float(moneyAmountDepositing)
      print("You have " + str(balanceMoney[username]) + " in your account")
    elif option == "2":
      moneyTakenAway = input("How much would you like to withdrawal? Only 0 to how much have right now.")
      balanceMoney[username] -= float(moneyTakenAway)
      print("You have " + str(balanceMoney[username]) + " in your account.")
    elif option == "3":
      oldPassword = input("To change your password, please type in your old password: ")
      if oldPassword != information[username]:
        print("The password you have put in is invalid.Please try again.")
    elif option == "4":
      break
    else:      
        newPassword = input("Type in the new password: ")
        information[username] = newPassword
        print("Your password has been changed succcesfully.")
      
  else:
    for i in range(1,5):  
      break
  
  
