l1 = [a, b, c]
if len(l1) == len(set(l1)):
    print('no solution')
else: print(max(set(l1), key=l1.count))
