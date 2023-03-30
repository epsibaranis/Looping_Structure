# tranfers the n by n matrix
import random
n=int(input('n=?'))
b=[]
i=0
for ib in range (n):
    a=[]
    for j in range (n):
        x=random.randint(0,10)
        a.append(x)
    b.append(a)
print("n*n matrixes",b)
print("tranfers the n by n matrix")
for i in range(n):
    for j in range(n):
        print(b[j][i],end=' ')
    print()
