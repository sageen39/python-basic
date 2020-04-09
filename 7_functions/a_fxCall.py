# 1. create a function and call this function
print('\n1 ---call a Function---')


# step 1: define your fx
def greetingFx():
    print('Hello! Greeting from Function')


# Call your function
greetingFx()

# 2. function with args and params
print('\n2 ---call a Function with parameters---')


def names(firstName, lastName):
    print('First Name', firstName)
    print('Last Name', lastName)


# call your function
names('Sageen', 'Suwal')


# 3 fx with default value
print('\n3 ---call a Function with parameters---')
def defaultNames(firstName='Nepali', lastName='Babu'):
    print('First Name:', firstName)
    print('Last Name:', lastName)

# call your function
defaultNames()
defaultNames('sageen','suwal')


# 4 fx with return value
print('\n3 ---call a Function with return value---')
def add(a,b):
    total = a + b
    return total

#Function Call
print(add(10,4))
