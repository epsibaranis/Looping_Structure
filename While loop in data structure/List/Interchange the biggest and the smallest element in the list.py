# Interchange the biggest and the smallest element in the list
a=[]
n=int(input('n=?'))
i=0
while i<n:
    x=int(input('x=?'))
    a.append(x)
    i+=1
print("Before Interchanging the list",a)
i=0
b=0
s=9999999999
while i<n:
    if a[i]>b:
        b=a[i]
        p1=i
    if a[i]<s:
        s=a[i]
        p2=i
    i+=1
a[p1]=s
a[p2]=b
print("Interchange the biggest and the smallest element in the list",a)
