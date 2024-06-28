thistuple = ('apple', 'banana', 'cherry', 'apple', 'banana')
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1, tuple2, tuple3)


tuple1 = ("abc", 34, True, 40, "male")


mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

thistuple = tuple(("apple", "banana", "cherry")) 
print(thistuple)

#tuple update 
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ('apple', 'banana', 'cherry')
y = ('orange',)
thistuple += y
print(thistuple)
