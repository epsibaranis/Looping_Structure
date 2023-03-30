# Biggest and Smallest number of n random numbers
import random
n=int(input('n='))
b=0
s=1001
for i in range(n):
    x=random.randint(0,1000)
    print(x)
    b=x if x>b else b
    s=x if x<s else s
print('Biggest of n random number',b)
print('Smallest of n random number',s)
