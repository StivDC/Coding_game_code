######
#This code goes through 9 rows of numbers ranging  1- 9.
#It will create a new line of new numbers that haven't been printed before in their vertical row.

a=['a']*9
s=''
for i in range(9):
    t=input()
    for j in range(9):
        a[j] += t[j]
for i in range(9):
    for j in range(1,10):
        if not str(j) in a[i]:s+=str(j)
print(s)