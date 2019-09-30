import sys
import math

a = input() # Finished progress part of bar
b = input() # Ufinished progress part of bar
l = int(input()) #Length of bar
prog = float(input()) # Current progress of bar

r = a * math.ceil(prog*l) + b * math.floor(l*(1-prog))

print(r)
