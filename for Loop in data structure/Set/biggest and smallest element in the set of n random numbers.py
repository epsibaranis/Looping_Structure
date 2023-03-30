# biggest and smallest element in the set of n random numbers
import random
n=int(input('n=?'))
a=set()
for i in range(n):
    a.add(random.randint(0,100))
print("set",a)
b=0
s=9999
for i in a:
    b=i if i>b else b
    s=i if i<s else s
print('Biggest element:',b)
print('Smallest element:',s)
