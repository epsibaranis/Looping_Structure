# set of n random numbers
import random
n=int(input('n=?'))
a=set()
for i in range(n):
    a.add(random.randint(0,100))
print("set",a)
print("print it element by element")
for i in a:
    print(i)
