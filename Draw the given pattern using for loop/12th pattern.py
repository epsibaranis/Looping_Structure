"""
      *
     * *
    *   *
   *     *
  *       *
 *         *
* * * * * * * print the pattern using for loop
"""
print("print the pattern using for loop")
print(' '*6+'*')
j=5
m=1
for i in range(5):
    print(' '*j+'*'+' '*m+'*')
    j-=1
    m+=2
print('* '*7)
