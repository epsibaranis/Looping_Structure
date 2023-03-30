# No of Vowels and consonents in a string
n=input('n=')
l=len(n)
v=0
c=0
print("No of Vowels and consonents in a string using for loop")
for i in range(l):
     if n[i]=='a' or n[i]=='A' or n[i]=='e' or n[i]=='E'or n[i]=='i' or n[i]=='I' or n[i]=='o'or n[i]=='O' or n[i]=='u' or n[i]=='U':
         v+=1
     else:
         c+=1
print('Vowels in string=',v)
print('Consonents in string=',c)
