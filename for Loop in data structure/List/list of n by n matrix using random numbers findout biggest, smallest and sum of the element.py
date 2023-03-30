# list of n by n matrix using random numbers findout biggest, smallest and sum of the element
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
s=0
d=0
c=11
for i in b:
      for j in i:
          d=j if j<d else d
          c=j if j>c else c
          s=s+j
print('biggest element:',d)
print('smallest element:',c)
print('sum of the element',s)
