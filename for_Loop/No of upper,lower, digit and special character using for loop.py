# No of upper,lower, digit and special character using for loop
n=input('n=')
z=len(n)
u=0
l=0
d=0
e=0
s=0
print("No of upper,lower, digit and special character using for loop")
for i in range(z):
     if n[i].isupper():
         u+=1
     elif n[i].islower():
         l+=1
     elif n[i].isdigit():
         d+=1
     elif n[i].isspace():
         e+=1
     else:
         s+=1
print('no of uppercase=',u)
print('no of lowerccase=',l)
print('no of digit=',d)
print('no of empty space=',e)
print('no of Special character=',s)
