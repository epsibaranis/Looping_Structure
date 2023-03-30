# Count the number of positive, negative, zeroes in n random numbers
import random
n=int(input('n='))
a=0
b=0
c=0
for i in range(n):
    x=random.randint(-1000,1000)
    print(x)
    if x>0:
        a+=1
    elif x<0:
        b+=1
    else:
        c+=1
print('Numbers of positive number',a)
print('Numbers of Negative numbers',b)
print('Numbers of Zeroes',c)
