n = int(input())
d=[]
a,b=1,0
for i in range(0, n):
 d.append(b)
 a,b =b,a+b
print(*d)
