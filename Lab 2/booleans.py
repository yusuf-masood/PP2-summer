#boolean
print(bool('hello'))
print(bool(15))

#two variables
x = 'hello'
y = 15
print(bool(x))
print(bool(y))

bool('abc')
bool(123)
bool(['apple', 'cherry', 'banana'])

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


#function
class myclass():
    def len(self):
        return 0 
    
myjob = myclass()
print(bool(myjob))


def myFunction():
    return True
print(myFunction())

def myfunction():
    return True
if myfunction():
    print('yes')
else:
    print('No!')


x = 2000
print(isinstance(x, int))