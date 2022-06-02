#wap to filter all 5 divisibles from the given list
"""lst=[10,14,20,25,30,11]
result = list(filter(lambda x: (x % 5 == 0), lst))
print("Numbers of the said list divisible by 5 are:",result)"""

#wap to fetch only the even numbers of a list
"""lst=[10,14,20,25,30,11]
result =list(filter(lambda x:(x%2==0),lst))
print("Numbers of the said list divisible by 2 are:",result)"""

#wap to fetch the value 3 from a list
"""
lst=[10,14,20,25,30,11,13,3]
lst2=[]
for i in range(0,len(lst)):
     if (lst[i]==3):
         lst2.append(lst[i])
print(lst2)
"""

#wap to fetch from the list the number that starts with 3
"""
lst=[10,14,20,25,30,11,33,23,253]
lst2=[]
for i in lst:
    i=str(i)
    if str(i)[-1]=='3':
        print(i)
lst=[10,14,20,25,30,11,33,23,253]
lst2=[]
for i in lst:
    if i%10==3:
        lst2.append(i)
print(lst2)
for i in lst:
    i=str(i)
    if i.endswith('3'):
        lst2.append(int(i))
print(lst2)"""


"""day=str(input("enter tthe dat:"))
if day in ['monday','tuesday','wednesday',"thursday"]:
    print("wear uniform")
elif day=='friday':
    print("white and white")
elif day=='saturday':
    print("wear civil dress")
elif day=='sunday':
    print("ask mother")
else:
    print("invalid key")"""

#wap to print the elements starting with the letter p and ends with the letter n
"""lst=['python',190,'jumbo']
lst2=[]
for i in lst:
    i =str(i)
    if i[0]=='p' and i[-1]=='n':
        lst2.append(str(i))
print(lst2)
 """
#wap to fetch only the string type from a list
"""lst=[10,'a',10.3,True,'d',5,'c']
lst2=[]
for i in lst:
    if type(i)==str:
        lst2.append(i)
print(lst2)"""

#wap to fetch all the positive odd numbers from the list
"""lst=[10,20,33,-20,-30,-40,-67]
lst2=[]
for i in lst:
    if (i%2!=0 and i<0):
        lst2.append(i)
print(lst2)"""

#wap to fetch all palindromes from the list
"""fruits = ["apple", "banana", "cherry", "kiwi", "mango",'madam']
newlist = []
for x in fruits:
    if x[0]==x[-1]:
        newlist.append(x)
print(newlist)"""
#wap to fetch the smallest palind====rome word from the list





#wap to fetch all non palindrome words from the list
"""fruits = ["apple", "banana", "cherry", "kiwi", "mango",'madam']
newlist=[]
for x in fruits:
    if x[0]!=x[-1]:
        newlist.append(x)
print(newlist)"""

#wap to fetch the biggest non palindrome number from the list




#wap to fetch a word which starts with the letter a
"""fruits = ["apple", "banana", "cherry", "kiwi", "mango",'madam']
newlist=[]
for x in fruits:
    if x[0] =='a':
        newlist.append(x)
print(newlist)"""

#wap to fetch the word which contains the letter i
"""fruits = ["apple", "banana", "cherry", "kiwi", "mango",'madam']
newlist=[]
for x in fruits:
    if x[] in 'i':
        newlist.append(x)
print(newlist)"""


#wap to delete the duplicate characters in all palindrome words into  a new list





#wap to fetch all non palindrome words which starts with d
"""fruits = ["apple", "banana", "cherry", "kiwi", "mango",'madam','dax']
newlist = []
newlist1=[]
for x in fruits:
    if x[0]!=x[-1]:
        newlist.append(x)
print(newlist)
for x in newlist:
    if x[0]=='d':
        newlist1.append(x)
print(newlist1)"""


#wap to fetch all palindrome words which contain d at the middle
fruits = ["apple", "banana", "cherry", "kiwi", "mango",'madam']
print(fruits)
fru=[]
for i in fruits:

        fru.append(i)
print(fru)
#wap to fetch the biggest palindrome and smallest non palindrome words into a new list









#wap to display the missed numbers in the given list
"""lst=[1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20]
lst1=range(1,21)
lst2=[]
for i in lst1:
    if i not in lst:
        lst2.append(i)
print(lst2)
"""
#wap toget the center element from the list
"""
lst=[1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20]
if len(lst)%2==0:
    print(lst[(len(lst)//2)-1],lst[len(lst)//2])
else:
    print(lst[len(lst)//2])

#wap to add missing element in the list which contain 1 to 10
lst=[1,2,3,4,6,8,9,10]
for i in range(1,11):
    if i not in lst:
        lst.append(i)
print(lst)
"""
#wap to get the next element of each element
"""lst=[1,3,5,7,9]
lst1=[]
for i in lst:
    lst1.append(i)
    lst1.append(i+1)
print(lst1)"""

#wap to get reverse of the words
"""st="pathikani naresh yadav"
st1=st.split()
print(' '.join(st1[-1::-1]))
#wap to reverse the string
print(st[-1::-1])"""
#wap to reverse the characters of every word
"""st="pathikani naresh yadav"
st1=st.split()
print(st1)
st2=[]
for i in st1:
    st2.append(i[-1::-1])
    st3=' '.join(st2)
print(st3)"""

#wap to fetch all vowels from  a string
st=str(input("enter the word:"))
st1=[]
for i in st:
    if i in 'aeiouAEIOU':
        st1.append(i)
print(st1)
print(''.join(st1))

#wap to fetch all consonents from  a string
"""st="pathikani naresh yadav"
st1=[]
for i in st:
    if i not in  'aeiouAEIOU':
        st1.append(i)
print(st1)
print(''.join(st1))"""


