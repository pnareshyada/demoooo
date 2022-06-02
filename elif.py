"""print('exam results')
marks = 92
if marks==35:
    print('you are promoted marks:',marks)
elif marks>35:
    print('you passed the exam ')
    if marks>75 and marks<= 85:
        print('you got good marks:',marks)
    elif marks>85 and marks<=95:
        print('you got great marks:',marks)
    elif marks > 95:
        print('you got very good marks:', marks)
    else:
        print('betterluck next time',marks)
else:
    print('you failed',marks)"""




lst=[1,3,7,5,2,6,4]
ls2=[]
for i in lst:
    for j in lst:
        if (i+j)==7:
            ls2.append(i)
print(ls2)

