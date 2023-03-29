# draw the pattern shown below
"""
*
**
***
****
*****
******
*****
****
***
**
*   """
c=0
n=1
while c<=5:
    f=0
    while f<n:
        print('*',end='')
        f=f+1
    n=n+1
    c=c+1
    print()
d=0
q=5
while d<=5:
       e=0
       while e<q:
           print('*',end='')
           e=e+1
       q=q-1
       d=d+1
       print()
