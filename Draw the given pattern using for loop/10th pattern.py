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
     * print the pattern using for loop
"""
print("print the pattern using for loop")
j=1
m=9
for i in range(6,0,-1):
    print(' '*i+'*'*j)
    j+=2
for i in range(2,7):
    print(' '*i+'*'*m)
    m-=2
