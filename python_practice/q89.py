class Person:
    def __init__(self):
        pass
    def getGender(self):
        print("print the gender")

class Male(Person):
    def getGender(self):
        print("He is male")

class Female(Person):
    def getGender(self):
        print("She is Female")