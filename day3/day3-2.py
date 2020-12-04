import sys
from math import prod


class slope1 :
    def __init__(self, I):
        self.c=0
        self.i=0
        self.I=I

    def next(self, l, N):
        self.i += self.I
        self.i %= N
        if l[self.i]=='#' : self.c+=1
    
class slope5 :
    def __init__(self):
        self.c=0
        self.i=0
        self.j=True

    def next(self, l, N):
        self.j = not self.j
        if not self.j : return

        self.i+=1
        self.i%=N
        if l[self.i]=='#' : self.c+=1

with open(sys.argv[1]) as input :
    slopes = [slope1(1), slope1(3), slope1(5), slope1(7), slope5()]
    it=iter(enumerate(input))
    N=len(next(it)[1])-1 # don't care for the first row

    for j,l in it :
        for s in slopes :
            s.next(l, N)

    ps = [s.c for s in slopes]
    print(ps, prod(ps))
