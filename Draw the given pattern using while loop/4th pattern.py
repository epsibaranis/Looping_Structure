# print that pattern shown below
"""
******
*****
****
***
**
*   """
d=0
n=6
while d<=5:
    c=0
    while c<n:
        print('*',end='')
        c=c+1
    n=n-1
    d=d+1
    print() 
