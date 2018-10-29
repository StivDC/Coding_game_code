n=input()
m=input()
for i in range(0,len(n)):
    print((0,1)[n[i]=="1" and m[i]=="1"],end="")
