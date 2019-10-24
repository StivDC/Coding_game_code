#my first proper gen expression
#prints sum of ascii for each character in an input
print(sum(ord(c)for c in input()))
# Gathers binary equivilant in 7bits and strips out the 0b
to_bin = lambda c: bin(ord(c))[2:].zfill(7) 
