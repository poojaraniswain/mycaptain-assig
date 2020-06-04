n=int(input("enter the number of items"))
lst=list(map(int,input("enter the number").strip().split()))[:n]
for item in lst:
  if(item>0):
    print(item,end='')
