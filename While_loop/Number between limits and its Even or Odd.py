# Number between limits and its Even or Odd
a=int(input('a='))
b=int(input('b='))
print("The number between the limits and its Even or odd:")
while a<=b:
    if a%2==0:
      print(a,'Even')
    else:
      print(a,'Odd')
    a=a+1
