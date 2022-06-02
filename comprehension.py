"""list=[10,20,30,40]
print(tuple([i*i for i in list]))
print([i*i for i in list])
print({i*i for i in list})"""

"""
st='tuple loves the couple'
st=st.split()
print([len(i) for i in st])"""

"""st ="tuple loves the couple"
st=st.split()
print(st)
print([i for i in st if st[i]=='s'])"""

list=[1,3,3,4,4,4]
#print(filter(lambda
for i in list:
    ls=[]
    for j in list:
        if list[i]==list[j]:
            ls.append(i)
print(ls)