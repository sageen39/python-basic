animals = ["lion", "tiger", "dog", "parrot"]

## Using for loop
# Alternative 1
print("\nFor loop Alternative 1:")
for i in animals:
    print("->",i)


# Alternative 2
# Using range method and nested for loop
print("\nFor loop Alternative 2:")

length = len(animals) # getting length of list

for i in range(length): # Iterating the index
    print("=>"+ animals[i])
    for i in range(1,2):  # Iterating the index
        print("==>>" + animals[i])