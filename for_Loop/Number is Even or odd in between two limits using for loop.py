# Number is Even or odd in between two limits using for loop
a=int(input('a='))
b=int(input('b='))
for i in range (a+1,b):
    if i%2==0:
     print('Number is Even Number',i)
    else:
     print('Numbers is Odd Number',i)
