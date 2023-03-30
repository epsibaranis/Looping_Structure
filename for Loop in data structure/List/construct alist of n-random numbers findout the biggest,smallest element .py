# construct alist of n-random numbers findout the biggest,smallest element 
import random
a=[]
b=0
s=999999999
n=int(input('n=?'))
for i in range(n):
    x=random.randint(0,1000)
    a.append(x)
print(a)
for i in a:
    b=i if i>b else b
    s=i if i<s else s
print("Biggest element in the list",b)
print("Smallest element in the list",s)
