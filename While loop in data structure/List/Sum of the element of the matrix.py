# Sum of the element of the matrix
import random
n=int(input('n=?'))
b=[]
i=0
while i<n:
    r=0
    a=[]
    while r<n:
        x=random.randint(0,1000)
        a.append(x)
        r+=1
    b.append(a)
    i+=1
print("n*n matrix",b)
i=0
s=0
while i<n:
    j=0
    while j<n:
        s=s+b[j][i]
        j+=1
    i+=1
print('Sum of the matrix element=',s) 
