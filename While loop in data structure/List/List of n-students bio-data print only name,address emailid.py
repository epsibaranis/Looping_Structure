#List of n-students bio-data print only name,address emailid
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
print("List of n-students bio-data print only name,address emailid")
i=0
while i<n:   
    print('Name   : ',b[i][0])
    print('Address: ',b[i][3])
    print('Emailid: ',b[i][4])          
    i+=1
