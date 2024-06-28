thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#using while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


#join tuples
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 3, 2, 3, 4, 5)
tuple3 = tuple1 + tuple2
print(tuple3)

tuple = tuple1 = ("apple", "banana", "cherry")
mytuple = tuple*2
print(mytuple)