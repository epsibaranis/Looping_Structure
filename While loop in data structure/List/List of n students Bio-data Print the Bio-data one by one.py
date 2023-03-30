#List of n students Bio-data Print the Bio-data one by one
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
print("List of n students Bio-data Print the Bio-data one by one")
i=0
while i<n:
    j=0
    while j<n:
            print(b[i][j])
            j+=1
    i+=1
