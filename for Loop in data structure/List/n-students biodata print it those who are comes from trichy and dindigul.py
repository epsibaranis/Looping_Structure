# n-students biodata print it those who are comes from trichy and dindigul
n=int(input('n=?'))
b=[]
for i in range(n):
    a=[]
    x=input('Nmae   : ')
    y=input('Age    : ')
    c=input('Gender : ')
    d=input('Address: ')
    e=input('Emailid: ')
    a.append(x)
    a.append(y)
    a.append(c)
    a.append(d)
    a.append(e)
    b.append(a)
print("n-students biodata",b)
print("print it those who are comes from trichy and dindigul")
for i in range(n):
    for j in range(5):
        if b[i][j]=='trichy'or b[i][j]=='dindigul':
           print(b[i])
