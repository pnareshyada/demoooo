""""""
######################################3
# program to read write the file data
"""fileobj=open('sdfghjkl.txt','w')
fileobj.write('welcome naresh python language\n')
fileobj.write('welcome naresh python language\n ')
fileobj.write('welcome naresh python language')
"""
"""fileobj.close()
fileobj=open('sdfghjkl.py','a')
fileobj.write('welcome')
fileobj.close()"""

# wap to read all data from the file
"""fileobj=open('sdfghjkl.txt','r')
fileData=fileobj.read()
print(fileData)"""

#wap to write the data into the file
"""fileobj=open('sdfghjkl.txt','w')
fileobj.write("welcome to the python classes \n")
fileobj.close()"""

#wap to read the first to lines of the data
"""fileobj=open('sdfghjkl.txt','r')
fileData=fileobj.read(2)
print(fileData)

fileobj=open('sdfghjkl.txt','r')
fileData=fileobj.read()
print(fileData)"""

#wap a program to read the firstline of thw file
"""
a=open('sdfghjkl.txt','r')
b=a.readline()
print(b)
#or
print(open('sdfghjkl.txt','r').readlines()[0])"""

#wap a program to read the firstline of thw file
"""
a=open('sdfghjkl.txt','r')
b=a.readline()
print(b)
#or
print(open('sdfghjkl.txt','r').readlines()[2])"""

#wap to read the first word from the file line
"""a=open('sdfghjkl.txt','r')
b = a.readline()
print(b)
c = b.split(',')
print(c[0])
#or"""


#wap to read the last word from the last line
#wap to read the first word from the each line
#wap to read the first characte from second word in the third line
#wap to read the last character of second word in second line
#wap to read the first two characters from third word in first line

"""a=open('nareshnew.txt','r')
b=a.readline()
c=b.split(',')
print(b)
print(c[0])"""
#print(c)"""
#program to write into a file
#fileobj=open('nareshnew.txt','w')
#fileobj.write('welcome, naresh ,to ,learn ,python ,language')


#wap to read the last word from the last line
"""a=open('nareshnew.txt','r')
b=a.readlines()
print(b[-1].split(','))"""

"""print(open('nareshnew.txt','r').readlines()[0])#.split(',')[0][-2])
a=open("nareshnew.txt",'r')
b=a.readlines()
print(b)"""


#wap to count the all vowels in the file
"""a=open('nareshnew.txt','r')
b=a.read()
print(b)
v= 'aeiouAEIOU'
d ={}.fromkeys(v,0)
print(d)
for  i in b:
    if i in d:
        d[i]=d[i]+1
print(d)"""

#wap t oread all the words which contain 4 or above 4 characters
"""a=open("nareshnew.txt",'r')
b=a.readlines()
print(b)
newlist=[]
for i in b:
    c=i.split(',')
    for i in c:
        if len(i)>=4:
            newlist.append(i)
print(newlist)
"""
#wap to read all words which starts with tany vowel
"""a=open("nareshnew.txt",'r')
b=a.readlines()
print(b)
list=[]
for i in b:
    c=i.split(',')
    for i in c:
        if i[0] in 'aeiouAEIOUp':
            list.append(i)
print(list)"""

#wap to reverse all words which contain 'a' character

"""a=open("nareshnew.txt",'r')
b=a.readlines()
print(b)
list=[]
for i in b:
    c=i.split(',')
    for i in c:
        if 'a' in i:
            i=i.replace('\n','')
            x=i[-1::-1]
            list.append(x)
print(list)"""

#wap to read all the unique upper case characters from the list
a=open("nareshnew.txt",'r')
b=a.readlines()
print(b)
list=[]
for i in b:
    c=i.split(',')
    for i in c:
        for j in i:
            if j.islower()==True:
                list.append(j)
print(list)
