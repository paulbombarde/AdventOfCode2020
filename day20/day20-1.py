import sys
from copy import copy

tiles = {}
class Tile:
    def __init__(self, i):
        self.id = i
        self.data = []
        self.top = -1
        self.bottom = -1
        self.left = -1
        self.right = -1

    def parse(self,it):
        for l in it :
            if 1 == len(l) : break
            self.data.append(l.rstrip())

    def flipped(self) :
        r = Tile(self.id)
        for l in self.data :
            r.data.append(l[::-1])
        return r

    def rotated(self) :
        r = Tile(self.id)
        l = len(self.data)-1
        for i in range(len(self.data[0])) :
            r.data.append(''.join(d[l-i] for d in self.data))  
        return r

    def __str__(self) :
        return "Tile "+str(self.id)+"\n"+"\n".join(self.data)

    def check(self) :
        print("check",self.id)
        l = len(self.data[0])-1
        h = len(self.data)
        for i,ts in tiles.items() :
            if i == self.id : continue
            #print("checking",i, ts[0].id)

            real = None
            if self.left < 0 :
                for t in ts :
                    if 0 < t.right : continue
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

            if not real and self.right < 0 :
                for t in ts :
                    if 0 < t.left : continue
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

            if not real and self.top < 0 :
                for t in ts :
                    if 0 < t.bottom : continue
                    match = self.data[0] == t.data[h-1]
                    if match :
                        #print("match top", t.id)
                        self.top = t.id
                        real = t
                        real.bottom = self.id
                        break

            if not real and self.bottom < 0 :
                for t in ts :
                    if 0 < t.top : continue
                    match = self.data[h-1] == t.data[0]
                    if match :
                        #print("match bottom", t.id)
                        self.bottom = t.id
                        real = t
                        real.top = self.id
                        break

            if real :
                #print("match bottom")
                tiles[i] = [real]
                real.check()


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
for i,ts in tiles.items() :
    print(i, len(ts))

tiles[last_id][0].check()
prod = 1
for i,ts in tiles.items() :
    nb = 0
    t = ts[0]
    if t.left   < 0 : nb+=1
    if t.right  < 0 : nb+=1
    if t.top    < 0 : nb+=1
    if t.bottom < 0 : nb+=1

    if nb > 1 :
        print(i)
        prod *= i
print(prod)

