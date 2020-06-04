'''code for assigning element to list'''

n=int(input("enter the number of items"))
lst=list(map(int,input("enter the number").strip().split()))[:n]
'''accessing element from tuple'''
tup=tuple(list)
for item in tup:
  print(item,end='')
'''dictionary'''
dict={}
d=int(input("enter the number of items"))
key=input("enter the key").strip().split()[:d]
value=input("enter the value").strip().split()[:d]
for i in range(d):
  dict[key]=value
while(true):
  del_key=input("print the key u want to delete")
  del dict[del_key]
  cont=input("do u want to delete more...yes/no")
  if(cont=='yes'):
    continue
  else:
    break

  
