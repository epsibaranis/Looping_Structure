# Year between limits and its Leap year or not
a=int(input('a='))
b=int(input('b='))
print("The year between the limits and it's leap year or not:")
while a<=b:
    if a%4==0:
             print(a,'Leap year')
    else:
        print(a,'Not leap year')
    a=a+1
