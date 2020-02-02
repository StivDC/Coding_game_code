l = input()
k=l.split(" ")
for i in k:
    if k.count(i) % 2 != 0:
        print(i)
        break
