

osList = ['Mac', 'Windows','Linux','Android']
print(osList[0:4])
print(osList[:4])


# using loop with slice list

for os in osList[0:4]:
     print("->"+os)

# copying lists using slicing lists

cpyOsList = osList[:]
print('Copied OS list:', cpyOsList)
