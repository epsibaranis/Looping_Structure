# difference of two n*n by matrix using list comprehension
import random
n=int(input('n=?'))
a=[[random.randint(0,10) for j in range(n)]for i in range(n)]
print("first n*n matrix",a)
b=[[random.randint(0,10) for j in range(n)]for i in range(n)]
print("second n*n matrix",b)
c=[[a[i][j]-b[i][j]for j in range(n)]for i in range(n)]
print("difference of two n*n by matrix",c)
