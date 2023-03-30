# construct a list of numbers 1 to 100 make all the odd numbers to 0 
a=[i if i%2==0 else 0  for i in range(0,101) ]
print("list of numbers 1 to 100 and all the odd numbers to 0",a)
