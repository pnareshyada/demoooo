#program to find the repeated number
array=[1,2,2,3,3,3,3]
print("duplicat values:")
for i in range(0,len(array)):
    for j in range(i+1,len(array)):
        if(array[i]==array[j]):
            print(array[i])


# program to print the average
"""n= int(input("enter the total number of elements you want to enter"))
sum =0
for i in range(n):
    x=int(input("enter the numbers:"))
    sum =sum+x
avg=sum/n
print("average:",avg)
"""
# program to find the sum of the all entered values
"""int(input("enter the number of values you want to enter:"))
sum =0
for i in range(n):
    x=int(input("enter the value:"))
    sum =sum+x
print("sum of numbera:",sum)"""

#program to print the area of a triangle
"""x=int(input("enter the length:"))
y=int(input("enter the breadth:"))
area=1/2*(x*y)
print("the area is :",area)"""


#program to print the area of a circle
"""r=int(input("enter the radius:"))
pi=3.14
area=pi*r*r
print("the area is :",area)
"""

#program to print the leap yaer
"""x=int(input("enter the year:"))
if x%4==0:
    print(x,"leap year")
else:
    print(x,"not leap year")"""

#calculator program

"""def calculator(n):
    s=0
    p=1
    a=int(input("enter the first value:"))
    b=int(input("enter the second value:"))
    if n==1:
        s=a+b
        print("sum:",s)
    elif n==2:
        s=a-b
        print("difference=",s)
    elif n==3:
        p=a*b
        print("product=",p)
    else:
        p=a/b
        print("result  is:",p)
i= int(input("enter the option\n"
             "1.add\n"
             "2.substaction\n"
             "3:multiplication\n"
             "4.divisiov\n"))
calculator(i)
"""

#progrm to print the reverse of a string
"""
string=(input("enter a string:"))
revstring=string[::-1]
print("the result is:",revstring)"""

#program to print the biggest num of the values
n=int(input("enter the number of values you want to enter:"))
l=[]
for i in range(n):
    n=int(input("enter the number :"))
    l.append(n)
big=0
for i in l:
    if i>big:
        big =i;

print("the biggest number is :",big)



