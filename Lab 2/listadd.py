thislist = ["apple", "banana", "cherry"]
thislist.append('orange')
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, 'melon')
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ['mango', 'pineapple', 'papaya']
thislist.extend(tropical)
print(thislist)

#remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("apple")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(2)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

