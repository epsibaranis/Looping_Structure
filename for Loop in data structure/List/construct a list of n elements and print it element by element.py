# construct a list of n elements and print it element by element
a=[]
n=int(input('n=?'))
for i in range(n):
    x=input('x=?')
    a.append(x)
print("list of n elements",a)
print("print it element by elemen")
for i in a:
    print(i)
