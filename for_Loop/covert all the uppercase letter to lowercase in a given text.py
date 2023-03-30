#covert all the uppercase letter to lowercase in a given text
s1=input('s1=?')
l=len(s1)
s2=''
for i in range(l):
    d=ord(s1[i])
    if d>=65 and d<=90:
        e=d+32
        a=chr(e)
        s2=s2+a
    else:
        b=chr(d)
        s2=s2+b
print("covert all the uppercase letter to lowercase in a given text",s2)
