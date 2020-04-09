thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#print specific value of key
print(thisdict["model"])


print("\n Editing Value of Year:")
thisdict["year"] = 2018
print(thisdict)

print("\nAdd Item in dictionary:")
thisdict["color"] = "red"
print(thisdict)

print("\nRemoving Item in dictionary:")
thisdict.pop("model")
print(thisdict)

print("\nCopying dictionary:")
mySeconddict = thisdict.copy()
print(mySeconddict)

print("\nClearing all Items in dictionary:")
thisdict.clear()
print(thisdict)

print("\nDelete dictionary:")
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.


