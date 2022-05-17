class Bird:
    def intro(self):
        print("There are different types of birds")

    def fly(self):
        print("Most of the birds can fly but some cannot")


class parrot(Bird):
    def intro(self):
        print('Hi, iam parrot')
    def fly(self):
        print("Parrots can fly")


class penguin(Bird):
    def fly(self):
        print("Penguins do not fly")


obj_bird = Bird()
obj_parr = parrot()
obj_peng = penguin()

obj_bird.intro()
obj_bird.fly()

obj_parr.intro()
obj_parr.fly()

obj_peng.intro()
obj_peng.fly()

