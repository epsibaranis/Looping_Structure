#find the frequency count of the numbers in a list using dictionary
import random
n=int(input('n=?'))
d={}
a=[random.randint(0,10)for i in range(n)]
print(a)
b=set(a)
for i in b:
    c=a.count(i)
    d[i]=c
print("dictionary",d)
m=int(input('m=?'))
print("Frequency count of the numbers in a list")
while(m!=5):
    print(d[m])
    m=int(input('m=?'))
