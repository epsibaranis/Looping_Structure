# List of a row big of n by n matrix
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
print(b)
i=0
c=[]
while i<n:
    j=0
    d=0
    while j<n:
        if b[i][j]>d:
            d=b[i][j]
        j+=1
    c.append(d)
    i+=1
print('The list of a row big in n by n matrix=',c)
