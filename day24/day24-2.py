import sys
from collections import defaultdict

tiles = defaultdict(bool)
i_min=10000000
j_min=10000000
i_max=-10000000
j_max=-10000000
print(tiles[0,0])

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

    i_min = min(i, i_min)
    i_max = max(i, i_max)
    j_min = min(j, j_min)
    j_max = max(j, j_max)
    tiles[(i,j)] = not tiles[(i,j)]
    #print(l.rstrip(),i,j,tiles[(i,j)])

c = sum(1 for i in tiles.values() if i)
print(c)

def next_state(i,j):
    c=0
    if tiles[(i+1, j+1)] : c+=1
    if tiles[(i+1, j-1)] : c+=1
    if tiles[(i-1, j+1)] : c+=1
    if tiles[(i-1, j-1)] : c+=1
    if tiles[(i+2, j)] : c+=1
    if tiles[(i-2, j)] : c+=1

    if tiles[(i,j)] :
        return c == 1 or c == 2
    else :
        return c == 2
  
def print_tiles():
    print(i_min, i_max, j_min, j_max)
    for j in range(j_min, j_max+1):
        l = ""
        for i in range(i_min, i_max+1) :
            if i%2 == j%2 :
                if tiles[i,j] : l+="x"
                else: l+="o"
            else:
                l+=" "
        print(l)
            
#print_tiles()
#print("======")

for d in range(100):
    ntiles = defaultdict(bool)
    i_min -= 1
    j_min -= 1
    i_max += 1
    j_max += 1
    for j in range(j_min, j_max+1):
        for i in range(i_min, i_max+1) :
            if i%2 == j%2 :
                ntiles[(i,j)] = next_state(i,j)
    tiles = ntiles
    print('Day',d+1,sum(1 for i in tiles.values() if i))

#print_tiles()


