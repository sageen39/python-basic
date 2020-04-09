#tuple is a sequence of immutable python objects. Tubles are like lists but cannot be changed.
#Tuples use parentheses, whereas list use square brackets
# There is a way to change the value of tuples which is called overwriting.


tups = (200, 50)
print(tups)
print(tups[0])
print(tups[1])

#use for loop with tuple:

for tup in tups:
    print("->" + str(tup))


# To do overwriting with a tuple
tup = (1000, 250, 300)
print(tup)