# Generate n random Numbers
import random
n=int(input('n='))
print("Generate n random Numbers using for loop:")
for i in range(n):
    x=random.randint(0,1000)
    print(x)
