# Parent_1
class Parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # indent is important

    def display_person(self):
        print('Name', self.name, "\nAge:", self.age)

# Parent_2
class MenCharacter:
    def character(self):
        print("Physically Strong")

# Child Class
class Child(Parent, MenCharacter):
    pass  # child class will inherit all feature of parent class


## out of the class
# create object of Child
kid = Child('Sageen', 39)
kid.display_person()
kid.character()
