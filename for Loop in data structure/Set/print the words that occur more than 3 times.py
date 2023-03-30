# print the words that occur more than 3 times
s=' one month is past,another is begun, since merry bells rang out the during year, and buds of rarest gren began to peer, as if impatient for a warmer sun, and though the distanct hills are bleak and dun, the virgin snowdrop,like a lambent fire, pierces the cold earth with its green streaked spire and in dark woods, the wandering little one may find a primrose '
l=s.split()
print(l)
b=set(l)
m=[]
for i in b:
    d=[]
    c=l.count(i)
    d.append(i)
    d.append(c)
    m.append(d)
print('countof the the text:', m)
p1=0
for i in range(len(m)):
    if m[i][1]>=3:
        p1=i
        print('print the words that occur more than 3 times=',m[p1])
