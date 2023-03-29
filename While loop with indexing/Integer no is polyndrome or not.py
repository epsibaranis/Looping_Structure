#integer no is polyndrome or not
a=int(input('a=?'))
c=''
b=str(a)
n=len(b)
i=1
print("integer no is polyndrome or not")
while i<=n:
      c=c+b[-i]
      i=i+1
d=int(c)
if d==a:
    print('integer no is polyndrome')
else:
    print('integer no is not polyndrome')
