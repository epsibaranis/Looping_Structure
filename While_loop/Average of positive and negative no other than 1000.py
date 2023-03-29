#Average of positive and negative no other than 1000
c=int(input("c=?"))
a=0
b=0
c=0
d=0
f=0
print("Average of positive integers and negative integers ")
while c!=1000:
    print(c)
    if c>0:
        a=a+1
        b=b+c
    else:
        d=d+1
        f=f+c
        c=int(input("c=?"))
print("Average of the positive integer",a/b)
print("Average of the Negative integer",d/f)           
