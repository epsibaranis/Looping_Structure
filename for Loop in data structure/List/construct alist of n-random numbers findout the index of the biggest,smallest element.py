# construct alist of n-random numbers findout the index of the biggest,smallest element 
import random
a=[]
b=[]
b.append(0)
b.append(9999999999)
n=int(input('n=?'))
for i in range(n):
    x=random.randint(0,1000)
    a.append(x)
print(a)
for i in range(n):
    for j in b:
       p1=i if a[i]>b[j] else j
       p2=i if a[i]<a[j] else j
print("index of the biggest element",p1)
print("index of the smallest element",p2)
