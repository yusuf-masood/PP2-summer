thislist = ['apple', 'bannana', 'cherry']
print(thislist[1])

thislist = ['apple', 'bannana', 'cherry']
print(thislist[-1])

thislist = ['apple', 'bannana', 'cherry', 'orange', 'pineapple', 'grape', 'pear']
print(thislist[2:5])

thislist = ['apple', 'bannana', 'cherry', 'orange', 'pineapple', 'grape', 'pear']
print(thislist[:5])

thislist = ['apple', 'bannana', 'cherry', 'orange', 'pineapple', 'grape', 'pear']
print(thislist[2:])

thislist = ['apple', 'bannana', 'cherry', 'orange', 'pineapple', 'grape', 'pear']
print(thislist[-4:-1])

thislist = ['apple', 'bannana', 'cherry', 'orange', 'pineapple', 'grape', 'pear']
if 'apple' in thislist:
    print("yes, 'appple' is in list")

thislist = ['apple', 'bannana', 'cherry', 'orange', 'pineapple', 'grape', 'pear']
thislist[1] = 'dragon fruit'
print(thislist)

thislist = ['apple', 'bannana', 'cherry', 'orange', 'pineapple', 'grape', 'pear']
thislist[1:2] = ['dragon fruit', 'watermelon']
print(thislist)

thislist = ['apple', 'bannana', 'cherry', 'orange', 'pineapple', 'grape', 'pear']
thislist[1:3] = ['watermelon']
print(thislist)

thislist = ['apple', 'bannana', 'cherry', 'orange', 'pineapple', 'grape', 'pear']
thislist.insert(2, 'melon')
print(thislist)