class tooyoungtogetmarried:
    pass
class itstimetogetmarry:
    pass
class toooldtogetmarried:
    pass
class toomucholdtogetmarry:
    pass
class checkageerror:
    pass

n=eval(input("enter your age:"))
if n<0 and n>100:
    raise checkageerror("check age")
if n>=0 and n<=20:
    raise tooyoungtogetmarried("you are too young")
elif n>20 and n<=40:
    raise itstimetogetmarry("marrytime")
elif n>40 and n<=70:
    raise toooldtogetmarried("toooldto marry")
else:
    raise toomucholdtogetmarry("too old")
