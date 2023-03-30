# no's of +ve, -ve, zero's
import random
a=[]
n=int(input('n=?'))
i=0
while i<n:
    x=random.randint(-100,100)
    a.append(x)
    i+=1
print("list",a)
i=0
x=0
y=0
z=0
while i<n:
    if a[i]>0:
        x=x+1
    elif a[i]<0:
        y=y+1
    else:
        z=z+1
    i+=1
print(a)
print('Number of positive number',x)
print('Number of Negative number',y)
print('Number of zeroes',z)
