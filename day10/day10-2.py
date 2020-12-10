import sys
from collections import defaultdict

input = [int(l) for l in open(sys.argv[1])]
input.sort()
print(input)

nb = defaultdict(int)
nb[0] = 1
for i in input :
    nb[i] = sum((nb[j] for j in  range(i-3,i)))

print(nb)
print(nb[input[-1]])
