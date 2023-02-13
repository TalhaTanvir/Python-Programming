mylist = ["apple","mango","orange","banana","strawberry"]
print(mylist)
print(len(mylist))
print(type(mylist))
print(mylist[2])

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#operations on list

cars = ["honda","toyota","bmw","ford","skoda"]
print(cars)
cars[4] = "hyundai"
print(cars)
cars.append("wolkswegen")
print(cars)
cars.remove("bmw")
print(cars)
cars.pop(1)
print(cars)


num = [100, 50, 65, 82, 23,7,32]
num.sort()
print(num)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)


l = ["a",1,["acs"]]
print(l)