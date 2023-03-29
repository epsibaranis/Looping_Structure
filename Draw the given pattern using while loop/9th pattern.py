# print the pattern shown below
"""
***********
 *********
  *******
   *****
    ***
     *
"""
c=0
q=0
n=11
while c<=5:
          s=0
          while s<q:
                   print(' ',end='')
                   s=s+1
          x=0
          while x<n:
                   print('*',end='')
                   x=x+1
          print()
          q=q+1
          n=n-2
          c=c+1
