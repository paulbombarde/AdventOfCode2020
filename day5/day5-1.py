import sys
from math import floor, ceil

with open(sys.argv[1]) as input :
    max_id = 0
    for l in input :
        i_min = 0
        i_max = 127
        j_min = 0
        j_max = 7;
        l = l.rstrip()
        for c in l :
            if c == "B" :
                i_min = ceil((i_max + i_min)/2)
            elif c == "F" :
                i_max = floor((i_max + i_min)/2)
            elif c == "L" :
                j_max = floor((j_max + j_min)/2)
            elif c == "R" :
                j_min = ceil((j_max + j_min)/2)
        id = i_min * 8 + j_min
        print(l, i_min, i_max, j_min, j_max, id)
        max_id = max(id, max_id)

    print(max_id)
                
