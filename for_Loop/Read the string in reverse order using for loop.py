# Read the string in reverse order using for loop
n=input('n=?')
l=len(n)
print("Read the string in reverse order using for loop")
for i in range(l-1,-1,-1):
    print(n[i],end='')
print()
