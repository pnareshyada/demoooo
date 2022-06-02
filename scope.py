"""
local variable
def great():
    x="hello"
   print(x)
great()"""

"""def great():
    x='helllo'
    print(x)
    def sayit():
        print("from sayit ",x)
    sayit()

great()

def great():
    x='hello'
    return x
a= great()
print(a)
x=99

def example():
    x=999
    print('in fun ',x)

example()
print('outside fun',x)"""

#x=99

"""def example():
    global x
    x=999
    print('in fun ',x)

example()
print('outside fun',x)"""

x=99
y=0
def example():
    global x
    x=333
    global y
    y =999
    print("in fun x=",x)
    print("in func y",y)
example()
print("outside the x:",x)
print("outside the y:",y)
print(globals()['y'])