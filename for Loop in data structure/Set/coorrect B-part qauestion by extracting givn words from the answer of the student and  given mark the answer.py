# coorrect B-part qauestion by extracting givn words from the answer of the student and  given mark the answer
s1=input('s1=?')
l1=s1.split()
b1=set(l1)
s2=input('s2=?')
l2=s2.split()
b2=set(l2)
l4=len(b2)
m=b1&b2
l3=len(m)
if l3>=5 and l3<=10:
    print('6 marks')
if l3>=11 and l3<=20:
    print('8 marks')
if l3==l4:
    print('10 marks') 
