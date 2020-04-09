# while loop
i = 1
while i <= 6:
    print(i)
    i += 1

# using flag to stop while loop
print('\nusing flag to stop while loop')

i = ''
name = 'Write any name(q to quit):'

while i != 'q':
    i = input(name)



# infinite loop with break

while True:
    i = input('infinite Loop(q for quit):')
    if i == 'q':
        break
