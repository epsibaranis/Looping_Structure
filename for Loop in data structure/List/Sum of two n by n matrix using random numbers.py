# Sum of two n by n matrix using random numbers
import random
n=int(input('n=?'))
b=[]
for ib in range (n):
    a=[]
    for j in range (n):
        x=random.randint(0,10)
        a.append(x)
    b.append(a)
print("first n*n matrix",b)
d=[]
for i in range (n):
    c=[]
    for j in range (n):
        x=random.randint(0,10)
        c.append(x)
    d.append(c)
print("Second n*n matrix",d)
f=[]
for i in range(n):
    e=[]
    for j in range(n):
        g=b[i][j]+d[i][j]
        e.append(g)
    f.append(e)
print('sum of a and b matrixes=',f)
