# extract the unique value of the list
import random
n=int(input('n=?'))
a=[random.randint(0,100)for i in range(n)]
print("list a:",a)
b=set(a)
print("length of set b",len(b))
print("set b",b)
