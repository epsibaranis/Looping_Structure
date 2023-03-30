# remove all the articles from the sets
s=' one month is past,another is begun, since merry bells rang out the during year, and buds of rarest gren began to peer, as if impatient for a warmer sun, and though the distanct hills are bleak and dun, the virgin snowdrop,like a lambent fire, pierces the cold earth with its green streaked spire and in dark woods, the wandering little one may find a primrose '
l=s.split()
print(l)
b=set(l)
c={'a','an','the'}
print("difference of the set:",b-c)
