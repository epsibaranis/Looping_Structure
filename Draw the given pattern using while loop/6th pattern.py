#draw the pattern shown below
"""  *
    **
   ***
  ****
 *****
******  """
c=0
n=5
q=1
while c<=5:
    d=0
    while d<n:
        print(" ",end="")
        d=d+1
    f=0
    while f<q:
        print("*",end="")
        f=f+1
    print()    
    n=n-1
    q=q+1
    c=c+1
