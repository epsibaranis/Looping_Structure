# Product of two n by n matrix
import random
n=int(input('n=?'))
a=[]
i=0
while i<n:
    r1=0
    c=[]
    while r1<n:
        x1=random.randint(0,4)
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
        x2=random.randint(0,4)
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
        k=0
        q=0
        while k<n:
              q=q+a[i][k]*b[k][j]
              k+=1
        f.append(q)
        j+=1
    e.append(f)
    i+=1
print('Product of two n by n maririx= ',e)
