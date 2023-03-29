# Print Years from 1000 to 3000 and say the year is leap year or not
c=1000
while c<=3000:
    if c%4==0:
        print(c,'Leap year')
    else:
        print(c,'not Leap year')
    c=c+1
