# display the number other than 1000 and say it is positive, Negativr or not
c=int(input('c=?'))
print("display the number other than 1000 and say it is positive, Negativr or not")
while c!=1000:
    if c>0:
        print(c,'is Positive')
    elif c>0:
        print(c,'is negative')
    else:
        print(c,'is Zero')
    c=int(input('c=?'))
