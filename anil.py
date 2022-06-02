num=eval(input("enter the value:"))
if num%2==0:
    if num==0:
        print("enter value above 0")
    elif num>0 and num<=20:
        print(num,"is between 0 and 20" )
    else:
        print(num,"is above 20")
    print("the number is even")
elif num%2!=0:
    if num>0 and num<=20:
        print(num,"is between 0 and 20" )
    else:
        print(num,"is above 20")
    print("the number is not even")
elif num==0:
    print("enter the value above 0")
else:
    print("number")