# extract the unique value of the list
import random
n=int(input('n=?'))
a=[random.randint(0,10)for i in range(n)]
print("list a",a)
b=set(a)
print("set b:",b)
m=[]
for i in b:
    d=[]
    c=a.count(i)
    d.append(i)
    d.append(c)
    m.append(d)
print("unique value of the list",m)
d1=0
s1=999
p1=0
p2=0
for i in range(len(m)):
    if m[i][1]>d1:
        d1=m[i][1]
        p1=i
    if m[i][1]<s1:
        s1=m[i][1]
        p2=i
print('Highest occurence of the element:',m[p1])
print('lowest occurence of the element:',m[p2])
