#Read the string and it is polyndrome or not
a=input('a=?')
b=''
l=len(a)
for i in range(l,0,-1):
    b=b+a[-i]
if b==a:
    print('String is Polyndrome')
else:
    print('The string is not Ployndrome')
