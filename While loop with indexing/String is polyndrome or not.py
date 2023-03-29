# string is polyndrome or not
a=input('a=?')
b=''
n=len(a)
i=1
print("string is polyndrome or not")
while i<=n:
    b=b+a[-i]
    i=i+1
if b==a:
    print('string is polyndrome')
else:
    print('string is not polyndrome')
