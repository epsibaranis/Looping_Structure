# List of N students biodata Person by person
n=int(input('n=?'))
b=[]
i=0
while i<n:
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
    i+=1
print("List of N students biodata Person by person")
i=0
while i<n:
    print(b[i])
    i+=1
