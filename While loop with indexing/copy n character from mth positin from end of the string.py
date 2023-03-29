#copy n character from mth positin from end of the string
s1=input('s1=?')
m=int(input('m=?'))
n=int(input('n=?'))
s2=''
i=1
print("copy n character from mth positin from end of the string")
while i<=n:
    s2=s2+s1[-m]
    m=m+1
    i=i+1
print(s2)
