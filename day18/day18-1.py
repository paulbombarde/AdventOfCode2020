import sys

def apply(stack, v) :
    if stack[-1][1] == "+" :
        stack[-1][0] += v
    elif stack[-1][1] == "*" :
        stack[-1][0] *= v
    else :
        stack[-1][0] = v

def compute(line):
    stack = [[0, ""]]
    for e in line.split() :
        #print(stack, e)
        if e == "+" or e == "*" :
            stack[-1][1] = e
            continue

        while e.startswith("(") :
            stack.append([0, ""])
            e = e[1:]

        popcount = 0
        while e.endswith(")") :
            e = e[:-1]
            popcount += 1

        apply(stack, int(e))

        for i in range(popcount) :
            v = stack.pop()[0]
            apply(stack, v)

    return stack[0][0]

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


