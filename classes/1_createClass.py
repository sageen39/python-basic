class Person:

    def add_person(self, name, age, id_num):
        self.name = name
        self.age = age
        self.id_num = id_num

        # indent is important

    def display_person(self):
        print('\nPrint using Function call:')
        print('Name', self.name, "\nAge:", self.age, "\nId:", self.id_num)


## out of the class
# create object of Person Class
person = Person()
person.add_person('Sageen',39,121212)
person.display_person()

#Variable access
print('\nPrint using variable access:')
print('Id:',person.id_num)
print('Name:',person.name)
print('Age:',person.age)
