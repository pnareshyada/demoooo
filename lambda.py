"""x= lambda a,b :a+b
print(x(10,20))"""

"""y=lambda a,b:a if a>b else b
print(y(10,20))

lis= [10,2,23,25,45]
print(list(filter(lambda i : i%2==0,lis)))"""

"""lis=[20,90,98,78,45,30,80,456,30]
print(list(filter(lambda i:i%10==0,lis)))"""

"""str="qwerty naresh laptop"
str= str.split()
print(list(filter(lambda i:len(i)<=6,str)))"""

"""str="qwerty naresh laptop"
str=str.split()
print(list(filter(lambda i:'n' in i ,str)))"""

"""lis=[10,20,30,40]
print(list(map(lambda i: i+10,lis)))"""

"""lis=[1,2,3,4,5,6]
print(list(map(lambda i:i*i ,lis)))"""

"""lst=[10,2030,50,60,49]
from functools import reduce
print(reduce(lambda a,b : a if a>b else b, lst))"""

lst=[10,20,30,40,89]
from functools import reduce
print(reduce(lambda a,b: a+b ,lst))