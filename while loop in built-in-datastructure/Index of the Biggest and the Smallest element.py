#Index of the Biggest and the Smallest element
a=[]
n=int(input('n=?'))
i=0
while i<n:
    x=int(input('x=?'))
    a.append(x)
    i+=1
print("list",a)
b=0
s=9999999999
i=0
while i<n:
    if a[i]>b:
        b=a[i]
        p=i
    if a[i]<s:
        s=a[i]
        q=i
    i+=1
print('The Biggest element index',p)
print('The Smallest element index',q)
