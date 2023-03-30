#list of n random numbers
import random
random.seed(0)
n=int(input('n=?'))
a=[random.randint(0,10)  for i in range(n)]
print("list of n random numbers",a)
