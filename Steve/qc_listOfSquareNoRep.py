# Takes in string -2 1 0 1 2

# Initial solution

s = input().split(" ")
s = [int(i)**2 for i in s]
print(sorted(list(dict.fromkeys(s))))

# Optimised solution for code golf

print(sorted(list(dict.fromkeys([int(i)**2 for i in input().split(" ")]))))
