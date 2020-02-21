s=input()
t=[]
for i in s.split(" "): t.append(sum([*map(i.lower().count, "aeiou")]))
print(*t)
