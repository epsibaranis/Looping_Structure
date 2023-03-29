# Read the string and count the uppercase lower case digit and special character
x=input('x=?')
i=0
u=0
l=0
f=0
s=0
n=len(x)
print("count the uppercase lower case digit and special character in a string")
while i<n-1:
    print(x[i])
    d=ord(x[i])
    if d>=65 and d<=90:
        u=u+1
    elif d>=97 and d<=122:
        l=l+1
    elif d>=48 and d<=57:
        f=f+1
    else:
        s=s+1
    i=i+1
print('Uppercase',u)
print('Lowercase',l)
print('digit',f)
print('Special',s)
