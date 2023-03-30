# sum of two n*n matrix
import random
n=int(input('n=?'))
a=[]
i=0
while i<n:
    r1=0
    c=[]
    while r1<n:
        x1=random.randint(0,10)
        c.append(x1)
        r1+=1
    a.append(c)
    i+=1
print('First matrix=',a)

i=0
b=[]
while i<n:
    r2=0
    d=[]
    while r2<n:
        x2=random.randint(0,10)
        d.append(x2)
        r2+=1
    b.append(d)
    i+=1
print('Second  matrix=',b)

i=0
e=[]
while i<n:
    j=0
    f=[]
    while j<n:
        s=a[i][j]+b[i][j]
        j+=1
        f.append(s)
    e.append(f)
    i+=1

print('Sum of two  matrix=',e)
