# list of n by n matrix
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
print("list of n by n matrix",b)
