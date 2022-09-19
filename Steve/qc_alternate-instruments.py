
n = int(input())
a= []
for i in range(n):
    a+=[input()]

p = True
for i, b in enumerate(a):
    if i == n - 1 and b == "drums":
        print("tss")
    elif b == "guitar":
        if p:
            print("plinx")
        else:
            print("plonx")
        p = not p
    else:
        print("badum")
