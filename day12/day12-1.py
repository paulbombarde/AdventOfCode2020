import sys

os = ["E", "S", "W", "N"]
o = 0
i = 0
j = 0

for l in open(sys.argv[1]) :
    a = l[0]
    v = int(l[1:])
    print(a, v)

    if a == "F" :
        a = os[o]

    if a == "N" :
        i+=v
    elif a == "S" :
        i-=v
    elif a == "E" :
        j+=v
    elif a == "W" :
        j-=v
    elif a == "R" :
        v = v//90
        o += v
        o %= 4
    elif a == "L" :
        v = v//90
        o += 4 - v
        o %= 4

    print(o, i, j)
print(abs(i)+abs(j))
