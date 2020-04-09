## Nested + elif
# write a program to find the large number among a,b & c

#Alternative 1

a = 5
b = 50
c = 10

if a > b:
    if a > c:
        print(str(a) + " is Greater")
    else:
        print(str(c) + " is Greater")

elif b > c:
    print(str(b) + " is Greater")
else:
    print(str(c) + " is Greater")


## Alternative 2 : and or
if a > c and a > b:
    print(str(a) + " is Greater")
elif b > a and b > c:
    print(str(b) + " is Greater")
else:
    print(str(c) + " is Greater")
