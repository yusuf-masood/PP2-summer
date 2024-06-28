fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# loop through letters
for x in "banana":
  print(x)

# break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
# x as a word
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


# continue 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#range 
for x in range(6):
  print(x)


for x in range(2, 6):
  print(x)


for x in range(2, 30, 3):
  print(x)

# else in for loop 
for x in range(6):
  print(x)
else:
  print("Finally finished!")


# break when x 
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")    