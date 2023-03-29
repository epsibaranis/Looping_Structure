#print the pattern shown below
"""
     *
    ***
   *****
  *******
 *********
*********** """
c=0
n=5
q=1
while c<=5:
          s=0
          while s<n:
                   print(' ',end='')
                   s=s+1
          y=0
          while y<q:
                   print('*',end='')
                   y=y+1
          print()
          n=n-1
          q=q+2
          c=c+1
