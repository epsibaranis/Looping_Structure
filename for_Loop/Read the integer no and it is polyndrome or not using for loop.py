# Read the integer no and it is polyndrome or not using for loop
a=int(input('a=?'))
c=str(a)
b=''
l=len(c)
print("Read the integer no and it is polyndrome or not using for loop:")
for i in range(l,0,-1):
    b=b+c[-i]
if b==c:
    print('integer is Polyndrome')
else:
    print('The integer is not Ployndrome')
