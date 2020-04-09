thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print("\n Print all key names in the dictionary, one by one:")
for x in thisdict:
  print(x)

print("\n Print all key names in the dictionary, one by one:")
for x in thisdict.keys():
  print(x)


print("\n Print all values in the dictionary, one by one:")
for x in thisdict:
  print(thisdict[x])

print("\n Print all values in the dictionary, one by one:")
for x in thisdict.values():
  print(x)

print("\n Loop through both keys and values, by using the items() function:")
for x, y in thisdict.items():
  print(x, y)