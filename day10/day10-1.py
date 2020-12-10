import sys
from collections import defaultdict

input = [int(l) for l in open(sys.argv[1])]
print(input)
input.sort()
print(input)

prev = 0
nb = defaultdict(int)
for i in input :
    nb[i-prev] += 1
    prev = i
nb[3]+=1 # the device itself

print(nb)
print(nb[1]*nb[3])
