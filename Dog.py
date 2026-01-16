class Dog:
    def __init__(self, name, age):#init function
        self.name = name # Honda Pilot = name
        self.age = age
    def __str__(self):
        self.name
        myString = self.name + " is " + str(self.age) + " years old!"
        return myString
    def age_to_dogyears_oversimplified(self):
        return self.age*7 
myDog = Dog("Lion", 6)        
print(myDog)
print(myDog.age_to_dogyears_oversimplified())
mySecondDog = Dog("Spot", 3)
print(mySecondDog)