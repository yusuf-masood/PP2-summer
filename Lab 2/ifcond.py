a = 33
b = 200
if b > a:
  print("b is greater than a")

#elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#one line 
a = 2
b = 330
print("A") if a > b else print("B")

#one line if esle with 3 condition
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#if inside if 
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    