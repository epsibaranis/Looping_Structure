# Second Biggest element in the n-element list
a=[]
n=int(input('n=?'))
i=0
while i<n:
    x=int(input('x=?'))
    a.append(x)
    i+=1
print("list",a)
i=0
b=0
while i<n:
    if a[i]>b:
        b=a[i]
    i+=1
i=0
c=0
while i<n:
    if a[i]!=b:
        if a[i]>c:
            c=a[i]
    i+=1
print("Second Biggest element in the n-element list",c)
