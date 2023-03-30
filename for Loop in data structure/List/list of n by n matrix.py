# list of n by n matrix
import random
n=int(input('n=?'))
b=[]
for i in range (n):
    a=[]
    for j in range (n):
        x=random.randint(0,10)
        a.append(x)
    b.append(a)
print("list of n by n matrix using for loop",b)
