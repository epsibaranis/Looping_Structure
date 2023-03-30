# two sets of n random numbers and their union intersection difference
import random
n=int(input('n=?'))
a=set()
b=set()
for i in range(n):
    a.add(random.randint(0,10))
    b.add(random.randint(0,10))
print("set a:",a)
print("set b:",b)
print("union of set",a|b)
print("Intersection of set",a&b)
print("Difference of set",a-b)
