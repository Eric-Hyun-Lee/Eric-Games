UserInput  = input("Type in a number: ") # Ask for the user to enter a number
ReplacementBackwards = ""
for i in range(len(UserInput)):
    ReplacementBackwards+=UserInput[len(UserInput)-i-1]
    
print(int(ReplacementBackwards))
for i in range(2,45,3):
    print(i)