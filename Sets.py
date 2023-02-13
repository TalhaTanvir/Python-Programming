myset = {"apple","banana","mango","orange"}
print(myset)
print(type(myset))

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


mix = {"abc",123,True,4.2}
print(mix)
print(len(mix))

addset = {"apple", "banana", "cherry"}
addset.add("orange")
print(addset)

tropical = {"pineapple", "mango", "papaya"}
addset.update(tropical)
print(addset)