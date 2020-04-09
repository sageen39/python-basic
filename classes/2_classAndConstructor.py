class Person:

    def __init__(self, name, age, id_num):
        self.name = name
        self.age = age
        self.id_num = id_num

    # indent is important

    def display_person(self):
        print('Name', self.name, "\nAge:", self.age, "\nId:", self.id_num)


## out of the class
# create object of Person Class
person = Person('Sageen', 39, 121212)
person.display_person()
