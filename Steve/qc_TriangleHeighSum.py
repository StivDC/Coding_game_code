# For n blocks
# Calculate what the height of the triangle would be where the top of a triangle would have 1 block
# then 2 blocks etc untill there are no blocks left
# also print any remaining blocks if there are any

n = int(input())
if n == 0:
    print(0,0)
else:
    j = 1
    while j < n:
        n = n-j
        j+=1
    if j-n == 0:
        print(j, j-n)
    else:
        print(j-1, n)
        
# for n = 10
# output: 4, 0
