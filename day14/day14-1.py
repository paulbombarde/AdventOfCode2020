import sys
from collections import defaultdict

regs = defaultdict(int)
mask_or = 0
mask_and = 0
for l in open(sys.argv[1]) :
    if l.startswith("mask = ") :
        m = l[7:].rstrip()
        m_or = m.replace("X", "0")
        m_and = m.replace("X", "1")
        mask_or = int(m_or, 2)
        mask_and = int(m_and, 2)
        #print(m, m_or, m_and, mask_or, mask_and)
    else :
        [m,e,v]=l.split()
        r = int(m.split('[')[1][:-1])
        v = int(v)
        v |= mask_or
        v &= mask_and
        regs[r] = v

count = sum(v for r,v, in regs.items())
print(count)
