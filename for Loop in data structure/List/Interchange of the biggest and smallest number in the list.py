# Interchange of the biggest and smallest number in the list
a=[]
b=0
s=9999999999
p1=0
p2=0
n=int(input('n=?'))
for i in range(n):
    x=int(input('x=?'))
    a.append(x)
print(" Before Interchanging the list:",a)
for i in range(n):
    p1=(i if a[i]>p1 else p1) if a[i]>b else(b if b>a[p1] else p1)
    p2=(i if a[i]<p2 else p2) if a[i]<s else (s if s<a[p2] else p2)
a[p1]=s
a[p2]=b
print("Interchange of the biggest and smallest number in the list",a)
