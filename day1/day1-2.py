import sys

with open(sys.argv[1]) as input :
    vals = {int(v) for v in input}
    prods = {}
    for v in vals :
        for vv in vals :
            prods[vv+v] = vv*v

    for v in vals :
        try:
            print(v*prods[2020-v])
        except KeyError :
            pass
        
