import sys
from collections import defaultdict

class Rules :
    def __init__(self):
        self.rules = {}
        self.votes = []

    def parse(self, l) :
        name, ranges = l.split(":")
        for r in ranges.split():
            bounds = r.split("-")
            if not len(bounds) == 2 :
                continue
            key = (int(bounds[0]), int(bounds[1]))
            if key in self.rules.keys() :
                raise Exception("ERROR : twice same range")
            self.rules[key] = name

    def is_valid(self,ticket) :
        valid = True
        for i in ticket :
            found = False
            for (b0,b1),n in self.rules.items() :
                if b0 <= i and i <= b1 :
                    found = True
                    break
            if not found :
                valid = False
        return valid

    def detect_names(self, ticket) :
        # init for first use
        if not self.votes :
            self.nb_votes = 0
            self.votes = [defaultdict(int) for f in ticket]

        self.nb_votes += 1
        for i in range(len(ticket)):
            for (b0,b1),n in self.rules.items() :
                if b0 <= ticket[i] and ticket[i] <= b1 :
                    self.votes[i][n]+=1

    def select_valid_names(self) :
        for i in range(len(self.votes)) :
            invalid=[]
            for n,c in self.votes[i].items() :
                if not c == self.nb_votes :
                    invalid.append(n)
            for n in invalid :
                del self.votes[i][n]
            #print(i, self.votes[i])

        self.mapping = {}
        while not len(self.mapping) == len(self.votes) :
            f = ""
            for i in range(len(self.votes)) :
                if len(self.votes[i]) == 1 :
                    f = next(iter(self.votes[i].keys()))
                    self.mapping[f] = i
                    #print(f, i)
                    break
            for i in range(len(self.votes)) :
                try :
                    del self.votes[i][f]
                except KeyError :
                    pass

    def compute_dest_product(self, ticket):
        prod = 1
        for n,i in self.mapping.items() :
            if n.startswith("departure") :
                prod *= ticket[i]
        return prod


rules = Rules()
with open(sys.argv[1]) as input :
    lines = iter(input)

    print("## parsing rules")
    for l in lines :
        if len(l) == 1 : break
        rules.parse(l)

    print("## parsing my ticket")
    if not next(lines).startswith("your ticket:") :
        print("bad parse 1")
    my_ticket = [int(i) for i in next(lines).split(",")]
    rules.detect_names(my_ticket)

    if not len(next(lines)) == 1 :
        print("bad parse 2")

    print("## parsing nearby tickets")
    if not next(lines).startswith("nearby tickets:") :
        print("bad parse 3")

    for l in lines :
        ticket = [int(i) for i in l.split(",")]
        if rules.is_valid(ticket) :
            rules.detect_names(ticket)
rules.select_valid_names()
print(rules.compute_dest_product(my_ticket))

