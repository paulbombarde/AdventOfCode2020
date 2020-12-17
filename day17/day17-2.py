import sys
from collections import defaultdict

class Pocket :
    def __init__(self, source) :
        self.pocket = defaultdict(int) # what a waist...
        self.i_min=0
        self.i_max=0
        self.j_min=0
        self.j_max=0
        self.k_min=0
        self.k_max=1
        self.l_min=0
        self.l_max=1

        for i,l in enumerate(source) :
            self.i_max+=1
            self.j_max=len(l)+1
            for j,v in enumerate(l) :
                if v == "#" :
                    self.pocket[(i,j,0,0)]=1

    def epoch(self):
        self.i_min-=1
        self.i_max+=1
        self.j_min-=1
        self.j_max+=1
        self.k_min-=1
        self.k_max+=1
        self.l_min-=1
        self.l_max+=1
        for i in range(self.i_min, self.i_max) :
            for j in range(self.j_min, self.j_max) :
                for k in range(self.k_min, self.k_max) :
                    for l in range(self.l_min, self.l_max) :
                        n = self.neighbours(i,j,k,l)
                        v = self.pocket[(i,j,k,l)]%2
                        if (v and ( n == 2 or n == 3)) or ((not v) and n == 3) :
                            self.pocket[(i,j,k,l)] +=2
        for i in range(self.i_min, self.i_max) :
            for j in range(self.j_min, self.j_max) :
                for k in range(self.k_min, self.k_max) :
                    for l in range(self.l_min, self.l_max) :
                        v = self.pocket[(i,j,k,l)]
                        if 2 <= v :
                            self.pocket[(i,j,k,l)] =1
                        else:
                            self.pocket[(i,j,k,l)] =0
    
    def neighbours(self, I, J, K, L):
        n=0
        for i in range(I-1, I+2) :
            for j in range(J-1, J+2) :
                for k in range(K-1, K+2) :
                    for l in range(L-1, L+2) :
                        if i==I and j==J and k==K and l==L :
                            continue
                        if self.pocket[(i,j,k,l)]%2 :
                            n+=1
        return n

    def count(self):
        return sum(self.pocket.values())

    def print(self):
        for k in range(self.k_min, self.k_max) :
            for l in range(self.l_min, self.l_max) :
                print("z",k,"l",l)
                for i in range(self.i_min, self.i_max) :
                    s=""
                    for j in range(self.j_min, self.j_max) :
                        if self.pocket[(i,j,k,l)] :
                            s+='#'
                        else:
                            s+='.'
                    print(s)

    

with open(sys.argv[1]) as input:
    p = Pocket(input)
#p=Pocket([".#.","..#","###"])
#p.print()
print(0, p.count())
for b in range(6) :
    #print("\n#############################")
    p.epoch()
    #p.print()
    print(b+1, p.count())






