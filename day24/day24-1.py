import sys
from collections import defaultdict

tiles = defaultdict(bool)
for l in open(sys.argv[1]) :
    i=0
    j=0
    cs = iter(l)
    try :
        while 1 :
            c = next(cs)
            if c == 's' :
                j+=1
                if 'e' == next(cs) :
                    i+=1
                else:
                    i-=1
            elif c == 'n' :
                j-=1
                if 'e' == next(cs) :
                    i+=1
                else:
                    i-=1
            elif c == 'e' :
                i+=2
            else:
                i-=2
    except StopIteration :
        pass
    tiles[(i,j)] = not tiles[(i,j)]
    #print(l.rstrip(),i,j,tiles[(i,j)])

c = sum(1 for i in tiles.values() if i)
#for k,v in tiles.items():
#    print(k,v)
print(c)
