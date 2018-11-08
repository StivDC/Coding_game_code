########
#bitwise or
n1, n2 = input().split()
for x,c in zip(n1,n2):
        print(int(x) | int(c),end="")    
#bitwise and
n1, n2 = input().split()
for x,c in zip(n1,n2):
        print(int(x) & int(c),end="")    
