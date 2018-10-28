s1 = input()
s2 = input()
y = ""
for c in s1:
    for x in s2:
        if c == x:
            y += c
print(y.replace(" ",""))
y = [int(x) for x in str(y)]
y.sort
newstr = " ".join(str(e) for e in y)
print(newstr)
