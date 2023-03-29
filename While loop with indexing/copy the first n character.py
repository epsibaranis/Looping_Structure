# copy the first n character
s1=input('s1=?')
n=int(input('n=?'))
s2=''
i=0
print("copy the first n character")
while i<n:
    s2=s2+s1[i]
    i=i+1
print(s2)
