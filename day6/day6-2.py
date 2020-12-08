import sys
from collections import defaultdict 

with open(sys.argv[1]) as input :
    count = 0
    group = defaultdict(int)
    gl = []
    for l in input :
        l = l.rstrip()
        if len(l) == 0 :
            for k,v in group.items() :
                if v == len(gl) :
                    count += 1
            print(gl,group, count)
            group.clear()
            gl.clear()
        else:
            for c in l :
                group[c] += 1
            gl.append(l)
    count += len(group)
    print(gl,group,len(group), count)



