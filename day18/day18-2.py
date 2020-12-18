import sys
from operator import mul
from functools import reduce

def compute(line):
    stack = [[[], ""]]
    for e in line.split() :
        #print(stack, e)
        if e == "+" or e == "*" :
            stack[-1][1] = e
            continue

        while e.startswith("(") :
            stack.append([[], ""])
            e = e[1:]

        popcount = 0
        while e.endswith(")") :
            e = e[:-1]
            popcount += 1

        v = int(e)
        if stack[-1][1] == "+" :
            stack[-1][0][-1] += v
        else :
            stack[-1][0].append(v)
            

        for i in range(popcount) :
            v = reduce(mul, stack.pop()[0], 1)
            if stack[-1][1] == "+" :
                stack[-1][0][-1] += v
            else :
                stack[-1][0].append(v)
            

    #print("final", stack)
    return reduce(mul, stack[0][0], 1)

#print("1 + 2 * 3 + 4 * 5 + 6", compute("1 + 2 * 3 + 4 * 5 + 6"))
#print("1 + (2 * 3) + (4 * (5 + 6))", compute("1 + (2 * 3) + (4 * (5 + 6))"))
#print("2 * 3 + (4 * 5)", compute("2 * 3 + (4 * 5)"))
#print("5 + (8 * 3 + 9 + 3 * 4 * 3)", compute("5 + (8 * 3 + 9 + 3 * 4 * 3)"))
#print("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", compute("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))
#print("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", compute("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))

s = 0
for l in open(sys.argv[1]) :
    v = compute(l)
    s += v
    print(l.rstrip(), v, s)


