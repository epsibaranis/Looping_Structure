# index of the biggest and smallest element in the list
import random
a=[]
n=int(input('n=?'))
for i in range(n):
    x=random.randint(0,10000)
    a.append(x)
print(a)
b=max(a)
s=min(a)
p1=a.index(b)
p2=a.index(s)
print("Biggest element in the list:",b)
print("smallest element in the list:",s)
print("Index of the Biggest Element",p1)
print("Index of the smallest Element",p2)
