thisset = {"apple", "banana", "cherry"}
print(thisset)

#duplicate not allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#true and 1 are same
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#length of set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#type 
myset = {"apple", "banana", "cherry"}
print(type(myset))

#access to a set
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#existence 
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#Adding to set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#adding from one set to another
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


#remove from set
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#loop set
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)