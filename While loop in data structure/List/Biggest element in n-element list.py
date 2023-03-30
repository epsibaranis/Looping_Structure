# Biggest element in n-element list
a=[]
n=int(input('n=?'))
i=0
while i<n:
    x=int(input('x=?'))
    a.append(x)
    i=i+1
print("list",a)
b=0
i=0
while i<n:
    if b<a[i]:
        b=a[i]

    i=i+1
print("Biggest element in n-element list",b)
