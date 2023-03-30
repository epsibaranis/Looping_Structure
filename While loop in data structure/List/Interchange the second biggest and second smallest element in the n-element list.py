# Interchange the second biggest and second smallest element in the n-element list
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
    if a[i]<s:
        s=a[i]
    i+=1
i=0
c=0
d=9999999999
while i<n:
    if a[i]!=b:
       if a[i]>c:
           c=a[i]
           p1=i
    if a[i]!=s:
       if a[i]<d:
            d=a[i]
            p2=i
    i+=1
a[p1]=d
a[p2]=c
print("Interchange the second biggest and second smallest element in the n-element list",a)
