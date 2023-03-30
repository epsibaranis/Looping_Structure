# biggest and smallest element in the tuple
import random
random.seed(0)
n=int(input('n=?'))
a=tuple(random.randint(0,1000)for i in range(n))
print("Tuble",a)
b=0
s=9999
for i in a:
   b=i if i>b else b
   s=i if i<s else s 
print('biggest element:',b)
print('smallest element:',s)
