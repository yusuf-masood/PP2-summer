x = 'awesome'
def myfunc():
    print('python is ', x)
myfunc()

y = 'awesome'
def myfunc():
    y = 'fantastic'
    print('python is '+ y)
myfunc()
print('pytnon is '+y)

def myfunc():
    global z
    z = 'amazing'
    print('python is '+ z)
myfunc()
print('python is '+ z)