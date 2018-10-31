duration = input()
d=[]
y = ""
w = ""
for c in duration:
    d.append(c)
x = d[:2]
for c in x:
    y +=str(c)
x =d[3:]
for c in x:
    w +=str(c)
print(int(y)*60 + int(w))