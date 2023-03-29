# read the string and count the no of vowels and consonents
x=input('x=?')
n=len(x)
i=0
v=0
c=0
print("count the no of vowels and consonents in a string")
while i<=n-1:
    print(x[i])
    if x[i]=='a'or x[i]=='e'or x[i]=='i' or x[i]=='o' or x[i]=='u':
        v=v+1
    else:
        c=c+1
    i=i+1
print('vowel=',v)
print('consonants=',c)    
