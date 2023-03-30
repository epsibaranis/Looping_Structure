# Read the string concatenate in reverse order using for loop
a=input('a=?')
b=' '
l=len(a)
for i in range(l,0,-1):
    b=b+a[-i]
print(b)
