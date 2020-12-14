import sys
from collections import defaultdict

regs = defaultdict(int)
mask = 0

def apply_mask(i, r, v) :
    #print(mask, i, r, v)
    p = mask.find('X',i)
    if -1 == p :
        regs[r] = v
        print(r,v)
    else:
        b = 1<<(35 - p)
        apply_mask(p+1, r|b, v)
        b = (2<<36)-1-b
        apply_mask(p+1, r&b, v)
        
#test = ["mask = 000000000000000000000000000000X1001X",
#"mem[42] = 100",
#"mask = 00000000000000000000000000000000X0XX",
#"mem[26] = 1"]
#for l in test :
for l in open(sys.argv[1]) :
    if l.startswith("mask = ") :
        mask = l[7:].rstrip()
        base_mask = int(mask.replace("X", "0"), 2)
    else :
        [m,e,v]=l.split()
        r = int(m[4:-1]) | base_mask
        v = int(v)
        apply_mask(0, r, v)

count = sum(v for r,v, in regs.items())
print(count)
