# Index of the biggest element
a=[]
n=int(input('n=?'))
i=0
while i<n:
    x=int(input('x=?'))
    a.append(x)
    i+=1
print("list",a)
b=0
i=0
while i<n:
    if a[i]>b:
        b=a[i]
        p=i
    i+=1
print("Index of the biggest element in the list",p)
