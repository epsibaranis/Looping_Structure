# construct a list of numbers from 0 to 1000 that are divisible by 2,3,5,7
a=[i for i in range(0,1001)if i%2==0 or i%3==0 or i%5==0 or i%7==0]
print("list of numbers from 0 to 1000 that are divisible by 2,3,5,7",a)
