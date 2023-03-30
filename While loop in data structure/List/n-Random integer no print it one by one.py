# n-Random integer no print it one by one
import random
a=[]
n=int(input('n=?'))
i=0
while i<n:
    x=random.randint(-100,100)
    a.append(x)
    i+=1
print("Random number list",a)
print("print the list element by element")
i=0
while i<n:
    print(a[i])
    i+=1
