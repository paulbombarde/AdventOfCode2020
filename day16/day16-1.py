import sys

rules = {}
with open(sys.argv[1]) as input :
    lines = iter(input)

    print("## parsing rules")
    for l in lines :
        if len(l) == 1 : break
        name, ranges = l.split(":")
        name = name[:-1]
        for r in ranges.split():
            bounds = r.split("-")
            if not len(bounds) == 2 :
                continue
            rules[int(bounds[0])] = (int(bounds[1]), name)

    print("## parsing my ticket")
    if not next(lines).startswith("your ticket:") :
        print("bad parse 1")
    ticket = next(lines)
    print([int(i) for i in ticket.split(",")])

    if not len(next(lines)) == 1 :
        print("bad parse 2")

    print("## parsing nearby tickets")
    if not next(lines).startswith("nearby tickets:") :
        print("bad parse 3")

    error_rate = 0
    for l in lines :
        for i in l.split(",") :
            i = int(i)
            found = False
            for b0,(b1,n) in rules.items() :
                if b0 <= i and i <= b1 :
                    found = True
                    break
            if not found :
                #print("!!", i)
                error_rate += i

print("Error rate :",error_rate)

