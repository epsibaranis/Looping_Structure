# n-students biodata print it person by person
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
print("print it person by person")
for i in b:
    print(i)
