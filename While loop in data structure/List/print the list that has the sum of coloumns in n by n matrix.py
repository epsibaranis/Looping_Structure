# print the list that has the sum of coloumns in n by n matrix
import random
n=int(input('n=?'))
b=[]
i=0
while i<n:
    r=0
    a=[]
    while r<n:
        x=random.randint(0,100)
        a.append(x)
        r+=1
    b.append(a)
    i+=1
print("n*n matrixes",b)
i=0
c=[]
while i<n:
    j=0
    s=0
    while j<n:
        s=s+b[j][i]
        j+=1
    c.append(s)
    i+=1
print('The list has the sum of rows in n by n matrix=',c) 
