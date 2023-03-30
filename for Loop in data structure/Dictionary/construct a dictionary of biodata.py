#construct a dictionary of biodata
d={}
Rollno=int(input('Rollno=?'))
a=[]
n1=input('Name     :')
n2=input('Age      :')
n3=input('Education:')
n4=input('Address  :')
n5=input('Emailid  :')
a.append(n1)
a.append(n2)
a.append(n3)
a.append(n4)
a.append(n5)
d[Rollno]=a
print("dictionary of biodata",d)
