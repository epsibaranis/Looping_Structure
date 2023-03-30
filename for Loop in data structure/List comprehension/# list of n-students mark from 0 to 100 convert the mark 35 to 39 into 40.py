# list of n-students mark from 0 to 100 convert the mark 35 to 39 into 40
n=int(input('n=?'))
a=[int(input('x=?')) for i in range (n)]
print(" list of n-students mark from 0 to 100",a)
b=[40 if i>=35 and i<=39 else i for i in a]
print("convert the mark 35 to 39 into 40",b)
