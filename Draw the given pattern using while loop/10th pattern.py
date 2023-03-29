# print the pattern shown below
"""
     *
    ***
   *****
  *******
 *********
***********
 *********
  *******
   *****
    ***
     *
"""
c=0
n=5
q=1
while c<=5:
          s=0
          while s<n:
                   print(' ',end='')
                   s=s+1
          x=0
          while x<q:
                   print('*',end='')
                   x=x+1
          print()
          n=n-1
          q=q+2
          c=c+1

d=0
f=1
h=9
while d<=4:
          z=0
          while z<f:
                   print(' ',end='')
                   z=z+1
          y=0
          while y<h:
                   print('*',end='')
                   y=y+1
          print()
          f=f+1
          h=h-2
          d=d+1
