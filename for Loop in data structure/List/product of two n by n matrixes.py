# product of two n by n matrixes
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
print("second n*n matrix",d)
f=[]
for i in range(n):
    e=[]
    for j in range(n):
        q=0
        for k in range(n):
            q=q+b[i][k]*d[k][j]
        e.append(q)
    f.append(e)
print("product of two n by n matrixes",f)
