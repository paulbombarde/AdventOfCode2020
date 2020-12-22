import sys
from collections import deque

p1 = deque()
p2 = deque()
for l in open(sys.argv[1]) :
    if l.startswith("Player 1:"):
        p = p1
    elif l.startswith("Player 2:"):
        p = p2
    elif 1<len(l) :
        p.append(int(l))

while p1 and p2 :
    c1 = p1.popleft()
    c2 = p2.popleft()
    if c1 < c2 :
        p2.append(c2)
        p2.append(c1)
    else :
        p1.append(c1)
        p1.append(c2)

if p1 : p=p1
else: p=p2

s = sum((len(p)-i)*v for i,v in enumerate(p))
print(p, s)

