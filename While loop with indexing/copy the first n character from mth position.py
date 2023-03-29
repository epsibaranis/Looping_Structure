#copy the first n character from mth position
s1=str(input('s1=?'))
m=int(input('m=?'))
n=int(input('n=?'))
s2=''
i=0
print("copy the first n character from mth position")
while i<n:
    s2=s2+s1[m]
    i=i+1
    m=m+1
print(s2)
