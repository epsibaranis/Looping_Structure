# construct a list n  by n matrix print it row by row using random numbers
import random
n=int(input('n=?'))
b=[]
for i in range (n):
    a=[]
    for j in range (n):
        x=random.randint(0,10)
        a.append(x)
    b.append(a)
print("n*n matrixes",b)
print("print the list row by row using for loop")
for i in b:
          print(i)
