import sys
import math

a = input() # Finished progress part of bar
b = input() # Ufinished progress part of bar
l = int(input()) #Length of bar
prog = float(input()) # Current progress of bar

r = a * math.ceil(prog*l) + b * math.floor(l*(1-prog))

print(r)

###JAVASCRIPT VERSION

#const A = readline();
#const B = readline();
#const L = parseInt(readline());
#const prog = parseFloat(readline());

#// Write an action using console.log()
#// To debug: console.error('Debug messages...');


#console.log(A.repeat(prog*L+.9999|0)+B.repeat(L-(prog*L+.9999|0)));
