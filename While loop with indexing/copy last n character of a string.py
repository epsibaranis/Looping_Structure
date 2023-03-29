#copy last n character of a string
s1=input('s1=?')
s2=''
n=int(input('n=?'))
l=len(s1)
m=l-n
i=0
print("copy last n character of a string")
while i<n:
   s2=s2+s1[m]
   m=m+1
   i=i+1
print(s2)
