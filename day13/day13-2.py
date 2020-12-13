import sys

with open(sys.argv[1]) as input :
    min_time = int(input.readline())
    buses = input.readline().split(",")

#buses = ["7","13","x","x","59","x","31","19"]
#buses = ["67","7","59","61"]
#buses = ["67","x","7","59","61"]
#buses = ["67","7","x","59","61"]
lines = {int(l):t for t,l in enumerate(buses) if not l == "x"}

def found(T) :
    #print([T%l for l in lines.keys()])
    for l,o in lines.items() :
        if not (T + o)%l == 0 :
            return False
    return True

def brute():
    T=0
    fact = max(lines.keys())
    while not found(T) :
        T+=fact
    return T

def clever() :
    it = iter(lines.items())
    fact,t = next(it)
    for l,o in it :
        while not (t+o)%l == 0 : 
            t+=fact
        fact *= l
    return t

print(lines)
#print("brute", brute())
print("clever", clever())

