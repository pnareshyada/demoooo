"""c=1
while c<10:
    c = c + 1

    if c==3:
        print(c,'c value is now 3')
        continue

    if c==5:
        print(c,'c value is 5')
        break

    print(c, 'telugu computer world')"""

"""i=1
while i<=10:
    print(i)
    i=i+1"""

"""i=10
while i>=0:
    if i%2!=0:
        print(i)
    i=i-1
"""

"""n =eval(input("enter the table you want:"))
i=1
while i<=10 :
    print(n,"*",i,"=",n*i)
    i=i+1
"""
"""i=6
while i<=9:
    print(i)
    i=i+1"""

"""i=1
while i<=100:
    if i%10==0:
        print(i)
    i=i+1"""

"""for i in range(1,101,1):
    if (i%10==0):
        print(i)
"""
"""i=30
while i<=50:
    if (i%3==0):
        print(i)
    i=i+1
    """
"""for i in range(30,50,1):
    if(i%3==0):
        print(i)"""
i=10

"""while i>1:
    if i in [2,4,6,8]:
        i=i-1
        continue
    print(i)
    i=i-1"""
"""i=0
while i>1:
    if i in [2,4,6,8]:
        i=i-1
        continue
    elif i in (3,7):
        i=i-1
        break
    print(i)
    i=i-1"""


pwd='1234'
while True:
    pwd1=input("enter the password:")
    if pwd1==pwd:
        print("log in success")
        break
    else:
        print("you entered the wrong password")
        print("enter the correct password:")
        continue

"""pwd='1234'
while True:
    pwd1=input('enter the password:')
    if pwd==pwd1:
        print("log in success")
        break
    else:-000
        pass"""

"""d={'a':10,"b":20,"c":30}
print(d)
if d("b")==d:
    print("d is there")
else:
    print("d is not there")"Wwww