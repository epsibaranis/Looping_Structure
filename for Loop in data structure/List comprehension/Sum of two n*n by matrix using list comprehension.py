# Sum of two n*n by matrix using list comprehension
import random
n=int(input('n=?'))
x=[[random.randint(0,10) for j in range(n)]for i in range(n)]
print("first n*n matrix",x)
y=[[random.randint(0,10) for j in range(n)]for i in range(n)]
print("Second n*n matrix",y)
z=[[x[i][j]+y[i][j]for j in range(n)]for i in range(n)]
print(" Sum of two n*n by matrix",z)
