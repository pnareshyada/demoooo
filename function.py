#def sayhello(name,age):
  #  print('hello',name)
 #   print('age:',age)
#
#sayhello(age=30,name='naresh')


#def sayhello(name,age,country='india'):
 #   print('hello',name)
  #  print("age",age)
   # print("i am from",country)
#sayhello("naresh",19)
#sayhello("venky","america",23)
#sayhello("pinky",23,"pakistan")

"""

def add(*nums):
    result=0
    val =99
    for x in nums:
        result+= x
    return result ,val
numsum , z=add(10,20,30,40,0)
print(numsum,z)
"""
"""
n1=eval(input("enter the first number:"))
n2=eval(input("enter the second number:"))
def max(a,b):
    if a>b:
        print("{} is greater than the {} and {}".format(a,a,b))
    else:
        print("{} is greater than the {} and {}".format(b, a, b))
max(n1,n2)"""

"""char=eval(input("enter the string:"))
n=eval(input("how mant times you want to repeat:"))
def repeat(s,n):
    print(s*n)
repeat(char,n)"""
"""
list1=[10,20,3,32,3]
def evennum(list1):
    for i in list1:
        if i%2==0:
            print(i)
evennum(list1)
"""
"""st=input("enter a string:")
def fetchingVowels(st):
    list=[]
    for i in st:
        if i in 'aeiouAEIOU':
            list.append(i)
    print(list)
fetchingVowels(st)

list=[12,122,1,2,1,21]
def div(list):
    lis=[]
    for i in list:
        if i%3==0:
            lis.append(i)
    print(lis)
div(list)
"""

"""list=[10,20,30]
def squ(list):
    lis=[]
    for i in list:
        lis.append(i**2)
    print(lis)
squ(list)
"""

"""list=[10,20,30,40,60,90]
def even(list):
    lis=[]
    for i in list:
        if i%2==0 and i%3==0 :
            lis.append(i)
    print(lis)
even(list)"""

"""st="python is simlple and powerful"
def list1(st):
    lis=[]
    for i in st:
        if i=="n":
            lis.append(i)
        print(lis)
list1(st)"""

"""list=[3,5,2,8,13,433,22]
def odd(list):
    lis=[]
    for i in list:
        if i%2!=0:
            lis.append(i)
    print(lis)
odd(list)"""

"""list=[3,7,2,0,4,7]
def odd(list):
    odd=[]
    even=[]
    for i in list:
        if i==0:
            pass
        if i%2==0 :
            odd.append(i)
        else:
            even.append(i)
    print(odd)
    print(even)
odd(list)
"""

st='naresh new qwerty even'
st1=st.split()
print(st1)
def sp(st1):
    list=[]
    for i in st1:
        if i[0] in 'aeiou':
            list.append(i)
    [print(st1)
sp(st1)
#wap to display the all words contain a character two or more two times
"""st='naresh new qwerty even'
st =st.split()
def word(st):
    list=[]
    for i in st:
        if i.count('e')>=2:
            list.append(i)
    print(list)
word(st)"""

#wap to print the length of each word
"""st='naresh new qwerty even'
st=st.split()
def length(st):
    for i in st:
       print(i,'-',len(i))
length(st)"""





