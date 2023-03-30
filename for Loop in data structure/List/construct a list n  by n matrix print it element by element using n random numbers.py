# construct a list n  by n matrix print it element by element using n random numbers
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
print(" print the list element by element using for loop")
for i in b:
      for j in i:
          print(j,end=' ')
      print()
