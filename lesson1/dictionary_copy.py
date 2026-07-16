thisdict = {"author":"Charles", "title": "Growing money", "year": 2025}
mydict = thisdict
print(thisdict)
print(mydict)

print("\nafter using copy() function")
mydict = thisdict.copy()
thisdict["year"] = 2000
print(thisdict)
print(mydict)