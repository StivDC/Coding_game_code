l = input()
k=l.split(" ")
for i in k:
    if k.count(i) % 2 != 0:
        print(i)
        break

# Solution from another coder:
a = list(a)

x = 0
for y in a: x ^= y
print(x)
