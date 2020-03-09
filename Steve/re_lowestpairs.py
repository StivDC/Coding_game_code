k1=[]
k2=[]
for i in input().split():
    x = int(i)
    k1.append(x)
for i in input().split():
    y = int(i)
    k2.append(y)
    
k1.sort() // cheating way of getting smallest pairs from both lists
k2.sort()
k3=[] // the rest is the fiddly way of making the output precice to the way CoC wanted
for i, z in zip(k1, k2):
    k3.append((i,z))
print(*k3, sep = ", ") // didn't know about sep before
