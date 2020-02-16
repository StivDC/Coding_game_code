n = int(input())
line = [1]
for k in range(max(n,0)):             
    line.append(line[k]*(n-k)//(k+1))             
print(' '.join(str(v) for v in line))
