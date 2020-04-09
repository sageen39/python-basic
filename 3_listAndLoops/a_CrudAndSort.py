#adding element in list
animals = ["lion", "tiger", "dog", "parrot"]
print(animals)

# add element
animals.append('horse')
print("Appended List: ",animals)

# print specific animal from the list
print("\nSpecific Pick:")
print(animals[2].title())

# print from the end start from -1
print(animals[-1].title())

# change element
animals[3]= "cat"
print("\nChanged List: ",animals)


# Delete element
del animals[3]
print("Removed Element: ", animals)


## Sort the list

#Ascending
animals.sort()
print("\nAscending order", animals)

# Descending
animals.sort(reverse = True)
print("Descending order", animals)
# or
animals.reverse() # reverse from right to left
print("Ascending order", animals)