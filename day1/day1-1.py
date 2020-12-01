import sys

with open(sys.argv[1]) as input :
    vals = {int(v) for v in input}
    for v in vals :
        if 2020 - v in vals :
            print(v, 2020-v, (2020-v)*v)
        
