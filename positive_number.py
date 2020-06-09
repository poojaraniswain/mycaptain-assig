n=int(input("enter the number of items"))
lst=list(map(int,input("enter the number").strip().split()))[:n]
lst1=[]
for a in lst:
	if(a>0):
		lst1.append(a)
print(lst1)
