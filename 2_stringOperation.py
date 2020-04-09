#upper -> lower and vice versa
myNameDetail = "Sageen"

print(myNameDetail.lower())
print(myNameDetail.upper())

# capitalize
string = "all lower"
print(string.capitalize())

#to check if string is lower or upper
print(string.islower())
print(string.isupper())

print("\n################new line & tab####################\n")

# new line & tab
paragraph = "Kinds of fruits: \n\t 1. Apple \n\t 2. Pear \n\t 3. orange"
print(paragraph)


# Title Function
print("\n################ Title Function ####################\n")

firstName = "sageen"
lastName = "suwal"

print(firstName.title() + " " + lastName.title())


# convert integer to string using string function
print("\n####### convert integer to string using string function #######\n")

myNameDetail = "My name is Sageen and my age is "
age = 39
total = (myNameDetail + str(age))
print(total)

