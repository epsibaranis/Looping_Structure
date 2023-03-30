# tuple of n elements print it element by element
import random
n=int(input('n=?'))
a=(random.randint(0,100) for j in range(n))
print("Tuple",a)
print("tuple of n elements print it element by element")
for i in a:
    print(i)
