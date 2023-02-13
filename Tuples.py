tuple = ("apple", "banana", "cherry")
print(tuple)

t = (1)
print(type(t))
tu = (1,)
print(type(tu))

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))

mix = ("abc", 34, True, 40, "male")
print(mix)
print(mix[0])
print(mix[2:4])
print(mix[-1])


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)