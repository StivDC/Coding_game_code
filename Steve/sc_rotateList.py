d=[]
n=input() # for shift of list - 1 shifts list left one
n=input()
for i in input().split():
 d.append(i)
a= n %len(d)
d=d[-a:]+d[:-a]
print(*d)
