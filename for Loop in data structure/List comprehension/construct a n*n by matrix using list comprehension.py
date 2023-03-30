#construct a n*n by matrix using list comprehension
import random
n=int(input('n=?'))
x=[[random.randint(0,10) for j in range(n)]for i in range(n)]
print("n*n by matrix using list comprehension",x)
