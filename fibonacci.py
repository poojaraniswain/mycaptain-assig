n=int(input("eenter the number of elements"))
a,b=0,1
if(n==0):
  print(a)
elif(n==1):
  print(a,b)
else:
  print(a,b)
  for i in range(n):
    c=a+b
    print(c,end='')
    a=b
    b=c
