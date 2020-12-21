import sys
from copy import copy

tiles = {}
class Tile:
    def __init__(self, i):
        self.id = i
        self.data = []
        self.top = 0
        self.bottom = 0 
        self.left = 0
        self.right = 0

    def parse(self,it):
        for l in it :
            if 1 == len(l) : break
            self.data.append(l.rstrip('\n'))

    def flipped(self) :
        r = Tile(self.id)
        for l in self.data :
            r.data.append(l[::-1])
        return r

    def rotated(self) :
        r = Tile(self.id)
        for i in reversed(range(len(self.data[0]))) :
            r.data.append(''.join(d[i] for d in self.data))  
        return r

    def __str__(self) :
        return "Tile "+str(self.id)+"\n"+"\n".join(self.data)

    def check(self) :
        #print("check",self.id)
        l = len(self.data[0])-1
        h = len(self.data)
        for i,ts in tiles.items() :
            if i == self.id : continue
            #print("checking",i, ts[0].id)

            real = None
            if not self.left :
                for t in ts :
                    if t.right : continue
                    match = True
                    for p in range(h) :
                        if not self.data[p][0] == t.data[p][l] :
                            match = False
                            break
                    if match :
                        #print("match left", t.id)
                        self.left = t.id
                        real = t
                        real.right = self.id
                        break

            if not real and not self.right :
                for t in ts :
                    if t.left : continue
                    match = True
                    for p in range(h) :
                        if not self.data[p][l] == t.data[p][0] :
                            match = False
                            break
                    if match :
                        #print("match right", t.id)
                        self.right = t.id
                        real = t
                        real.left = self.id
                        break

            if not real and not self.top :
                for t in ts :
                    if t.bottom : continue
                    match = self.data[0] == t.data[h-1]
                    if match :
                        #print("match top", t.id)
                        self.top = t.id
                        real = t
                        real.bottom = self.id
                        break

            if not real and not self.bottom :
                for t in ts :
                    if t.top : continue
                    match = self.data[h-1] == t.data[0]
                    if match :
                        self.bottom = t.id
                        real = t
                        real.top = self.id
                        break

            if real :
                tiles[i] = [real]
                real.check()

    def nb_pattern_match(self, image):
        L = len(image[0])
        H = len(image)
        l = len(self.data[0])
        h = len(self.data) 
        coords=[]
        for J in range(L-l):
            for I in range(H-h):
                match = True
                for i in range(h):
                    for j in range(l):
                        if self.data[i][j] == "#" and not image[I+i][J+j] == "#" :
                            match = False
                            break
                if match : coords.append((I,J))
        return coords

    def stamp(self, image, coords):
        l = len(self.data[0])
        h = len(self.data) 
        for I,J in coords:
            for i in range(h):
                for j in range(l):
                    if self.data[i][j] == "#" :
                        image[I+i][J+j] = "O"

last_id = -1
with open(sys.argv[1]) as input :
    it = iter(input)
    while it :
        try :
            l = next(it)
            if not l.startswith("Tile "):
                raise Exception("Invalid Tile header")
            t = Tile(int(l[5:-2]))
            t.parse(it)
        except StopIteration :
            break

        r1 = t.rotated()
        r2 = r1.rotated()
        r3 = r2.rotated()
        f = t.flipped()
        f1 = f.rotated()
        f2 = f1.rotated()
        f3 = f2.rotated()
        tiles[t.id]=[t,r1,r2,r3,f,f1,f2,f3]
        last_id = t.id

# let's hope there is a single match for each pairs or borders
# consider the last one id correctly oriented
tiles[last_id]=[tiles[last_id][0]]

tiles[last_id][0].check()
for i in tiles.keys() :
    tiles[i]=tiles[i][0]

top_left = 0
for i,t in tiles.items() :
    if not t.left and not t.top :
        top_left = i
        break

first_in_line=i
final_image_ids = []
final_image = []
while first_in_line :
    ids = [first_in_line]
    while tiles[ids[-1]].right :
        ids.append(tiles[ids[-1]].right)
    for i in range(1,len(tiles[ids[0]].data)-1):
        l = []
        for j in ids :
            l.extend(tiles[j].data[i][1:-1])
        final_image.append(l)
    final_image_ids.append(ids)
    first_in_line = tiles[first_in_line].bottom

print(final_image_ids[0][0]*final_image_ids[-1][0]*final_image_ids[0][-1]*final_image_ids[-1][-1])

#for l in final_image_ids:
#    print(l)
#for l in final_image:
#    print(l)

m = Tile(-1)
m.parse([
"                  # ",
"#    ##    ##    ###",
" #  #  #  #  #  #   "])

def print_if_matches(pattern) :
    #print(pattern)
    n = pattern.nb_pattern_match(final_image)
    if n :
        pattern.stamp(final_image,n)
        c = sum(sum(1 for c in r if c == "#") for r in final_image)
        print(c)

print_if_matches(m)
m = m.rotated()
print_if_matches(m)
m = m.rotated()
print_if_matches(m)
m = m.rotated()
print_if_matches(m)
m = m.flipped()
print_if_matches(m)
m = m.rotated()
print_if_matches(m)
m = m.rotated()
print_if_matches(m)
m = m.rotated()
print_if_matches(m)
