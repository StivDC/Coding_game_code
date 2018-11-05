#Gathers two inputs
#First input is length, second is width
#Create a square with incrementing numbers using the width and height of r and c
#Square must be aligned properly, used to study alignment.
r = int(input())
c = int(input())
width = len(str((r*c)-1))+1
x = 0
toPrint = []
for i in range(r):
    tempPrint = ""
    for i in range(c):
        toAdd = str(x)
        while len(toAdd)<width:
            toAdd = " "+toAdd
        tempPrint += toAdd
        x+=1
    toPrint.append(tempPrint.rstrip())
for i in toPrint:
    print(i)