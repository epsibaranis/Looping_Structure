# construct a tuple of even numbers from 0 to 100
import random
n=int(input('n=?'))
a=tuple(random.randint(0,1000)for i in range(n))
print("Tuble",a)
b=tuple(i for i in a if i%2==0)
print("Tuple of even numbers",b)
