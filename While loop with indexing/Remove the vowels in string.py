#Remove the vowels in string
s1=input('s1=?')
s2=''
l=len(s1)
i=0
print("Remove the vowels in string")
while i<l:
    if s1[i]=='a' or s1[i]=='A' or s1[i]=='e' or s1[i]=='E' or s1[i]=='i' or s1[i]=='I' or s1[i]=='o' or s1[i]=='O' or s1[i]=='u' or s1[i]=='U':
        pass
    else:
        s2=s2+s1[i]
    i=i+1
print(s2)    
