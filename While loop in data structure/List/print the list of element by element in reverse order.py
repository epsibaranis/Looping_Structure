# print the list of element by element in reverse order
a=[]
n=int(input('n=?'))
i=0
while i<n:
    x=int(input('x=?'))
    a.append(x)
    i=i+1
m=1
print(a)
print("print the list of element by element in reverse order")
while m<=n:
    print(a[-m])
    m=m+1
