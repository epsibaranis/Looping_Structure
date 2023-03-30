# copy the n character from the end
s1=input('s1=?')
n=int(input('n=?'))
s2=''
l=len(s1)
for i in range(l-1,n+1,-1):
   s2=s2+s1[i]
print("copy the n character from the end in a string:",s2)
