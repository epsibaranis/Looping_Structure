# convert the uppercase to lowercase in string 
s1=input('s1=?')
s2=''
l=len(s1)
i=0
print("convert the uppercase to lowercase in string")
while i<l:
    d=ord(s1[i])
    if d>=65 and d<=90:
        e=d+32
        a=chr(e)
        s2=s2+a
    else:
        b=chr(d)
        s2=s2+b
    i=i+1
print(s2)
